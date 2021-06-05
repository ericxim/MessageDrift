from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    community_id = models.ForeignKey('Communities', models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=30)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    views = models.BigIntegerField(default=0)
    likes = models.BigIntegerField(default=0)
    
    
    
    def __str__(self):
        return self.content
    
class Communities(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    slug = models.SlugField(null=False, unique=True)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('view_community', kwargs={'slug':self.slug})

class Comments(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE)
    content = models.TextField()
    
    