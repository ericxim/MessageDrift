from django.db import models
from django.utils import timezone

class Post(models.Model):
    
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content