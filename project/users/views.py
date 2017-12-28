from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.shortcuts import render,  redirect
from django.views.generic import CreateView
from django.views.generic import UpdateView
from blogs.models import Blog
from posts.models import Post
from users.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm as BaseAuthenticationForm

def user_page(request, id):
    u = User.objects.get(id=id)
    blogs = Blog.objects.filter(user=id)
    ids = [blog.id for blog in blogs]
    posts = Post.objects.filter(blog__in=ids)
    return render(request, 'core/user_page.html', {'u': u, 'blogs': blogs, 'posts': posts})


def users_list(request):
    users = User.objects.all()[:10]
    return render(request, 'core/users_list.html', {'users': users})


class BlogUpdate(UpdateView):
    template_name = 'core/blog_update.html'
    model = Blog
    fields = 'title', 'description'
    pk_url_kwarg = 'blog_id'

    def dispatch(self, request, *args, **kwargs):
        print('here')
        if self.get_object().user == self.request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    # def get_queryset(self):
    #     return super(BlogUpdate, self).get_queryset().filter(user=self.request.user)

    def get_success_url(self):
        return reverse('blogs:blog', kwargs={'id': self.object.id})


class NewBlog(CreateView):
    template_name = 'core/new_blog.html'
    model = Blog
    fields = 'title', 'description'

    def get_success_url(self):
       return reverse("blogs:blog", kwargs={'id': self.object.id})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NewBlog, self).form_valid(form)


class AuthenticationForm(BaseAuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = "username", "password1", "password2"

    def label_tag(self, contents=None, attrs=None):
        pass

    def as_widget(self, widget=None, attrs=None, only_initial=False):
        pass

    def login(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('user_page', id=user.id)
        else:
            form = UserCreationForm()
            return render(request, 'core/login.html', {'form': form})


class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = get_user_model()
        fields = "username", "password1", "password2"

    def label_tag(self, contents=None, attrs=None):
        pass

    def as_widget(self, widget=None, attrs=None, only_initial=False):
        pass

    def signup(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('users:userpage', id=user.id)
        else:
            form = UserCreationForm()
        return render(request, 'core/signup.html', {'form': form})
