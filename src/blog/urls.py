"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include,url
from django.contrib import admin

''' Another way is :
from posts import views and the down url pattern would be url(r'^posts/$',views.post_home)
If there are more than one view that is imported from diffrent application then you write

from posts import views as posts_view
from contacts import views as contacts_view

and url would be url(r'^posts/$',post_view.post_home)
But this is not a preferred method.
'''

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include("posts.urls", namespace='posts')),
]
