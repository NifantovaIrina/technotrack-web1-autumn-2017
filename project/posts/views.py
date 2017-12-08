import datetime
from audioop import reverse

from django.forms import ModelForm, forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.views.generic import UpdateView

from blogs.models import Blog
from comments.models import Comment
from posts.form import NewComment
from posts.models import Post


def post(request, id):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=id)
    if request.method == "POST":
        form = NewComment(request.POST)
        form.instance.user_id = request.user.id
        form.instance.post_id = id
        if form.is_valid():
            form.save()
    form = NewComment()
    comments_num = comments.count()
    return render(request, 'core/post.html', {'post': post, 'comments': comments, 'num': comments_num,
                                              'form': form})


def posts_user(request, id):
    posts = Post.objects.filter(user=id).order_by(Post.likes)[:10]
    return render(request, 'core/posts_list.html', {'posts': posts})


def posts(request):
    posts = Post.objects.all().order_by('-date')[:10]
    return render(request, 'core/posts_list.html', {'posts': posts})



