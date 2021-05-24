from django.contrib import admin
from .models import Author, Post, PostCategory
# Register your models here.

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(PostCategory)
