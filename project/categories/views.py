from django.shortcuts import render
from categories.models import Category
from posts.models import Post


def category(request, id):
   c = Category.objects.get(id=id)
   posts = Post.objects.filter(category=id)
   return render(request, 'core/category.html', {'c': c, 'posts': posts})


def categories(request):
   categories = Category.objects.all()
   return render(request, 'core/categories.html', {'categories': categories})