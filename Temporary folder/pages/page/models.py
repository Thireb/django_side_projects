from django.db import models

# Create your models here.
class Page(models.Model):
    parmanent_links = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=20)
    published_date = models.DateTimeField("Published Date")
    text_area = models.TextField("Content",blank=True)
    def __str__(self):
        return self.title