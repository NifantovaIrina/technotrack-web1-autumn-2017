from django.conf.urls import url

from comments.views import comment

urlpatterns = [
    url(r'^comments/id(?P<id>\d+)/$', comment)
]
