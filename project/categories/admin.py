from django.contrib import admin
from categories.models import Category


@admin.register(Category)
class CategoryRegister(admin.ModelAdmin):
    pass