from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from posts import views
from posts.views import post, posts_user, posts

urlpatterns = [
    url(r'id(?P<id>\d+)/$', post, name='post'),
    url(r'^$', posts, name='posts'),
]