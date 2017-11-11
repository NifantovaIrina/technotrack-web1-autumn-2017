from django.conf.urls import url

from categories.views import category, categories

urlpatterns = [
    url(r'^id(?P<id>\d+)/$', category, name='category'),
    url(r'^$', categories, name='categories')
]