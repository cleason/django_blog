from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='publish')

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    
    def __str__(self):
        return self.name    

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_posts')
    STATUS_CHOICES = (
        ('brouillon', 'Brouillon'),
        ('publier', 'Publier'),
    )
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, default='brouillon', max_length=10)
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Posted')
    objects = models.Manager() # Default Manager
    publish = PublishedManager() # Custom manager
    
    class Meta:
        ordering = ['-published']
        verbose_name = ('Post')
        verbose_name_plural = ('Posts')
        
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        verbose_name = ('Comment')
        verbose_name_plural = ('Comments')
    
    def __str__(self):
        return self.post.title
    
