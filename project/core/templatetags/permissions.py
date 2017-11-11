from django import template
from blogs.models import Blog

register = template.Library()


@register.filter(name='has_permission')
def has_permission(user_id, blog_id):
    blog = Blog.objects.get(blog_id)
    return blog.user_id == user_id