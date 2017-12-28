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
    posts = Post.objects.all().order_by("-date_create")[:10]
    ids_posts = [post.blog_id for post in posts]
    blogs = Blog.objects.filter(id__in=ids_posts)
    ids_blogs = [blog.user_id for blog in blogs]
    users = User.objects.filter(id__in=ids_blogs)
    return render(request, 'core/base.html', {'posts': posts, 'blogs': blogs, 'users': users})
