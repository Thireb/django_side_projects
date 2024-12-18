from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model

# Create your models here.


STATUS_CHOICES = (
    ('NEW','New Site'),
    ('EX','Existing Site'),
)

PRIORITY_CHOICES = (
    ('U','Urgent -1 week or less'),
    ('N', 'Normal - 2 to 4 weeks'),
    ('L', 'Low - Still Searching'),
)

class Quote(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=60, blank=True)
    company = models.CharField(max_length=60, blank=True)
    address = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=30, blank=True) 
    email = models.EmailField()
    web = models.URLField(blank= True)
    description = models.TextField()
    sitestatus = models.CharField(max_length=20, choices=STATUS_CHOICES)
    priority = models.CharField(max_length=40, choices=PRIORITY_CHOICES)
    jobfile = models.FileField(upload_to='uploads/',blank= True)
    submitted = models.DateField(auto_now_add=True)
    quotedate = models.DateField(blank= True, null=True)
    quoteprice = models.DecimalField(max_digits=5, decimal_places=2, default=0, blank=True)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)