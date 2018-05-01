from django.urls import path
from django.conf.urls import url,include
from blog.views import post_detail


app_name = 'blog'

urlpatterns  = [
    url(r'^(?P<id>\d+)/$', post_detail,name='detail'),   
    #url(r'^$',all_post),
    #url(r'^new_post/',new_post),
]