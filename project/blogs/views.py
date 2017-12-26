from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import UpdateView, CreateView
from blogs.form import NewPost
from blogs.models import Blog
from posts.models import Post
from users.models import User


def blog(request, id):
    blog = Blog.objects.get(id=id)
    posts = Post.objects.filter(blog=id).order_by('-date_create')
    user = User.objects.get(id=blog.user_id)
    return render(request, 'core/blog.html', {'blog': blog, 'posts': posts, 'u': user})


# class BlogsListForm(forms.Form):
#     order_by = forms.CharField()
#     search = forms.CharField()
#
#
# class BlogsList(ListView):
#     template_name = 'core/blogs_list.html'
#     context_object_name = 'blogs_list'
#     model = Blog
#
#     def get_queryset(request):
#         form =

def blogs(request):
    blogs = Blog.objects.all().order_by('date_create')[:10]
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
    fields = 'title', 'text', 'categories'

    def dispatch(self, request, id=None, *args, **kwargs):
        self.blog = get_object_or_404(Blog.objects.all(), id=id)
        return super(NewPost, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        blog = Blog.objects.get(id=self.object.blog_id)
        return reverse('blogs:blog', kwargs={'id': blog.id})

    def form_valid(self, form):
        form.instance.blog = self.blog
        return super(NewPost, self).form_valid(form)

# def newPost(request, id):
#     if request.method == "POST":
#         form = NewPost(request.POST)
#         b = Blog.objects.get(id=id)
#         form.instance.blog = b
#         if form.is_valid():
#             form.save()
#     form = NewPost()
#     return render(request, 'core/new_post.html', {'form': form})