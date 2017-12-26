from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from blogs.views import blog, blogs
from blogs import views
urlpatterns = [
    url(r'^(?P<id>\d+)/$', blog, name='blog'),
    url(r'^$', blogs, name='blogs'),
    url(r'^(?P<id>\d+)/new_post/$', login_required(views.NewPost.as_view()), name='newpost'),
    # url(r'^(?P<id>\d+)/new_post/$', newPost, name='newpost'),
    url(r'^(?P<id>\d+)/edit/$', login_required(views.PostUpdate.as_view()), name='updatepost'),
]