from django.db import models
# Create your models here.

class Notif(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    debtAmount = models.IntegerField()
    debtDate = models.DateField()
    
    def __str__(self):
        return self.name