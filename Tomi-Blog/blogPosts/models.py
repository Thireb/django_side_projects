from django.db import models
from datetime import datetime
# Create your models here.

class Post(models.Model):

    title = models.CharField( max_length=150)
    body = models.CharField(max_length=5000)
    creation_date = models.DateTimeField(default= datetime.now, blank=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("post_detail", kwargs={"pk": self.pk})
