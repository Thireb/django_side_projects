from django.db import models
from django.contrib.auth.models import User
# Create your models here.
options = (
        ('Y', "YES"),
        ('N', "NO"),
    )
class QuoteModel(models.Model):
    name = models.CharField( max_length=50)
    email = models.EmailField(max_length=254)
    description = models.TextField()
    jawab = models.CharField(choices=options, max_length=20)
    submitted = models.DateField ( auto_now_add=True)
    money = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    username = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    jobfile = models.FileField(upload_to='Uploads/',blank=True)
    def __str__(self):
        return str(self.id)
    