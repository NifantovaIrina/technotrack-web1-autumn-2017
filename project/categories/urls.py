from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from categories import views
from categories.views import category, categories

urlpatterns = [
    url(r'^id(?P<id>\d+)/$', category, name='category'),
    url(r'^$', categories, name='categories'),
    url(r'^new_category/$', views.NewCategory.as_view(), name='newcategory')
]