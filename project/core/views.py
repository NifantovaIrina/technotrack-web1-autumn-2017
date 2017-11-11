from django.shortcuts import render
from  django.shortcuts import HttpResponse
# Create your views here.
# def postsList(request, id='100000'):
#     return render(request, 'posts_list.html', {'id': id})
#
# def userPage(request, id='100000'):
#     return render(request, 'user_page.html', {'id': id})
#
from blogs.models import Blog
from posts.models import Post
from users.models import User


def main(request):
    posts = Post.objects.order_by("-id").all()[:10]
    ids = [post.blog.id for post in posts]
    blogs = Blog.objects.filter(id__in=ids)
    return render(request, 'core/main_page.html', {'posts': posts, 'blogs': blogs})
