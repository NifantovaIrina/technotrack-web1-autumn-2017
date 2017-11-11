from django.contrib import admin

# Register your models here.
from blogs.models import Blog


@admin.register(Blog)
class BlogRegister(admin.ModelAdmin):
    pass