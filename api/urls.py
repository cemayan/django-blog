from django.urls import path
from django.conf.urls import url,include
from api import views
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'api'

urlpatterns  = [
    url(r'^$',views.PostList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),
    #url(r'^new_post/',new_post),
]

urlpatterns = format_suffix_patterns(urlpatterns)