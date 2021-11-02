from django.contrib import admin
from .models import BlogPost, Comment

admin.site.register((BlogPost, Comment))
