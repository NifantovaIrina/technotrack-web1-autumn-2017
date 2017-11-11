from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.views.generic import UpdateView
from blogs.models import Blog
from posts.models import Post


def blog(request, id):
    blog = Blog.objects.get(id=id)
    posts = Post.objects.filter(blog=id)
    return render(request, 'core/blog.html', {'blog': blog, 'posts': posts})


def blogs(request):
    blogs = Blog.objects.all().order_by('-id')[:10]
    return render(request, 'core/blogs_list.html', {'blogs': blogs})


class PostUpdate(UpdateView):
    template_name = 'core/post_update.html'
    model = Post
    fields = 'title', 'text'
    pk_url_kwarg = 'id'
    # def get_queryset(self):
    #     return super(PostUpdate, self).get_queryset().filter(id=self.kwargs.get('id'))

    def get_success_url(self):
        return reverse('posts:post', kwargs={'id': self.object.id})


class NewPost(CreateView):
    template_name = 'core/new_post.html'
    model = Post
    fields = 'title', 'text'

    def dispatch(self, request, id=None, *args, **kwargs):
        self.blog = get_object_or_404(Blog.objects.all(), id=id)
        return super(NewPost, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('posts:post', kwargs={'id': self.object.id})

    def form_valid(self, form):
        # form.instance.author = self.request.user
        form.instance.blog = self.blog
        return super(NewPost, self).form_valid(form)