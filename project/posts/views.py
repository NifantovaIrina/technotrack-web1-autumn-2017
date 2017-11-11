import datetime
from audioop import reverse

from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import UpdateView

from blogs.models import Blog
from comments.models import Comment
from posts.models import Post


def post(request, id):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=id)
    # blog = Blog.objects.get(id=post.objects.blog)
    return render(request, 'core/post.html', {'post': post, 'comments': comments})


def posts_user(request, id):
    posts = Post.objects.filter(user=id).order_by(Post.likes)[:10]
    return render(request, 'core/posts_list.html', {'posts': posts})


def posts(request):
    posts = Post.objects.all().order_by('-date')[:10]
    return render(request, 'core/posts_list.html', {'posts': posts})


