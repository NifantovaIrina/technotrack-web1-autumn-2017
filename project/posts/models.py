from django.db import models
from django.conf import settings

from blogs.models import Blog
from categories.models import Category


class Post(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey(Blog, default=None)
    categories = models.ManyToManyField(Category, blank=True)
    likes = models.IntegerField(default=0)