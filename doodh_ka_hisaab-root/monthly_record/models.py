from django.db import models
from django.utils import timezone

# Create your models here.
class Record(models.Model):
    Quantity = models.DecimalField( max_digits=5, decimal_places=2, default=3)
    Date_of_Current = models.DateField('Last Added', default=timezone.now())
    
