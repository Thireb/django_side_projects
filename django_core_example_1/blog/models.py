from django.db import models
from django.conf import settings
from datetime import datetime
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=122)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now())
    published_at = models.DateTimeField(blank=True,null=True)
    
    def publish(self):
        self.published_at = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title