from pyexpat import model
from re import search
from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'status', 'created', 'published', 'author')
    prepopulated_fields = {'slug': ('title',), }
    search_fields = ('title', 'body' )
    ordering = ('author', 'status', 'created')
    list_filter = ('author', 'created', 'published')

#admin.site.register(Post, AdminPost)
