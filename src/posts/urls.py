from django.conf.urls import url
from django.contrib import admin

from . import views


'''
if the 2 urls are same, then the url which is first, its function will be called first. So the top one takes the precedence.

      url(r'^create/$', "posts.views.post_detail"),
      url(r'^create/$', "posts.views.post_create"),

here even though its create url, detail function will be called.
'''

urlpatterns = [
    url(r'^$',   "posts.views.post_list"),
    url(r'^create/$', "posts.views.post_create"),
    url(r'^detail/$', "posts.views.post_detail"),
    url(r'^update/$', "posts.views.post_update"),
    url(r'^delete/$', "posts.views.post_delete"),


]

