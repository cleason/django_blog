from django.contrib import admin
from .models import Category, Post, Comment

# Register your models here.
@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'status', 'created', 'published', 'author')
    prepopulated_fields = {'slug': ('title',), }
    search_fields = ('title', 'body' )
    ordering = ('author', 'status', 'created')
    list_filter = ('author', 'created', 'published')


@admin.register(Comment)
class Comments(admin.ModelAdmin):
    list_display = ['username', 'email', 'created', 'updated',]
    
    
@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',), }