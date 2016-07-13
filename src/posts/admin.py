from django.contrib import admin

# Register your models here.

# .models - since both models and admin are in same directory
from .models import Post

admin.site.register(Post)