from django.db import models
from django.utils import timezone
import datetime
from django.contrib import admin

# Create your models here.


class Question(models.Model):

    question_text = models.CharField(max_length=250)
    published_at = models.DateTimeField('Date Published')
    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='published_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return  now - datetime.timedelta(days=1) <= self.published_at <= now
    
class Choice(models.Model):
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text