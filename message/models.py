from django.db import models
from django.utils import timezone

class Post(models.Model):
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    views = models.BigIntegerField(default=0)
    community_id = models.ForeignKey('Communities', models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.content
    
class Communities(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    