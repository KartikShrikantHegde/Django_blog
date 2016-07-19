from django.conf.urls import url
from django.contrib import admin

from .views import (
post_list,
post_create,
post_detail,
post_update,
post_delete,
)


'''
if the 2 urls are same, then the url which is first, its function will be called first. So the top one takes the precedence.

      url(r'^create/$', "posts.views.post_detail"),
      url(r'^create/$', "posts.views.post_create"),

here even though its create url, detail function will be called.
'''

urlpatterns = [
    url(r'^$',  post_list, name='list'),
    url(r'^create/$', post_create),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', post_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', post_delete),

]

