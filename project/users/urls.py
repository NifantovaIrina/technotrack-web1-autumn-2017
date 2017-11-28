from django.conf.urls import url
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from users import views
from users.views import user_page, users_list
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^(?P<id>\d+)/$', user_page, name="userpage"),
    url(r'^$', users_list, name="userslist"),
    # url(r'^login/$', login, {'template_name': 'core/login.html'}, name='login'),
    url(r'^login/$', LoginView.as_view(template_name='core/login.html'), name="login"),
    url(r'^logout/$', LogoutView.as_view(template_name='core/logout.html'), name="logout"),
    url(r'^signup/$', views.UserCreationForm.signup, name='signup'),
    url(r'^new_blog/$', login_required(views.NewBlog.as_view()), name='newblog'),
    url(r'^(?P<blog_id>\d+)/edit/$', login_required(views.BlogUpdate.as_view()), name='updateblog'),
]
