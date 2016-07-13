from django.contrib import admin

# Register your models here.

# .models - since both models and admin are in same directory
from .models import Post

# Creating an customized admin for the Polls app
# ModelAdmin is a class in Model

class PostModelAdmin (admin.ModelAdmin):
    # list_display is a django-admin keyword. other attributes match with model attributes
    list_display = ["title","updated","timestamp"]
    list_display_links = ["updated"]
    list_filter = ["updated","timestamp"]
    list_editable = ["title"]
    search_fields = ["title","content"]

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)