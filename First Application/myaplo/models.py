from django.db import models

# Create your models here.
class BlockModel:
    #model without django model class
    text: str
    
class SpaceModel(models.Model):
    text = models.CharField(max_length=255)
    
    def __str__(self):
        return self.text
    