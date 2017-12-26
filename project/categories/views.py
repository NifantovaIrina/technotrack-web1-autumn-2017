from django.urls import reverse
from django.shortcuts import render
from django.views.generic import CreateView

from categories.models import Category
from posts.models import Post


def category(request, id):
   c = Category.objects.get(id=id)
   posts = Post.objects.filter(categories=id)
   return render(request, 'core/category.html', {'c': c, 'posts': posts})


def categories(request):
   categories = Category.objects.all()
   return render(request, 'core/categories.html', {'categories': categories})


class NewCategory(CreateView):
   template_name = 'core/new_category.html'
   model = Category
   fields = ('name', )


   def get_success_url(self):
      return reverse('categories:categories')

   def form_valid(self, form):
      return super(NewCategory, self).form_valid(form)