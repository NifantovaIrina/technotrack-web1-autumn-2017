import string

from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from django.views.generic import UpdateView
from blogs.models import Blog
from users.models import User
from django.contrib.auth import get_user_model


def user_page(request, id):
    user = User.objects.get(id=id)
    blogs = Blog.objects.filter(user=id)
    return render(request, 'core/user_page.html', {'user': user, 'blogs': blogs})


# Последние 10 зарегистрировавшихся
def users_list(request):
    users = User.objects.all()[:10]
    return render(request, 'core/users_list.html', {'users': users})


class BlogUpdate(UpdateView):
    template_name = 'core/post_update.html'
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


class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = get_user_model()
        fields = "username", "first_name", "last_name", "password1", "password2", "email"

    def signup(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('main')
        else:
            form = UserCreationForm()
        return render(request, 'core/signup.html', {'form': form})
