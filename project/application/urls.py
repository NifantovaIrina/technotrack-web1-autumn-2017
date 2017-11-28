"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
# from core.views import posts, main, userPage, postsList
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.template.context_processors import static

from application import settings
from core.views import main

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main, name="main"),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^blogs/', include('blogs.urls', namespace='blogs')),
    url(r'^comments/', include('comments.urls', namespace='comments')),
    url(r'^categories/', include('categories.urls', namespace='categories')),
    url(r'^posts/', include('posts.urls', namespace='posts')),
]# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
