from django.db import models

# Create your models here.

class PagesModel(models.Model):
    """Model definition for PagesModel."""

    # TODO: Define fields here
    name = models.CharField('User name',max_length=255)
    date = models.DateField('Updated date',auto_now=True)
    permalink = models.CharField('Paragraph Link',unique=True,max_length=56)
    body = models.TextField('Body Text')
    # class Meta:
    #     """Meta definition for PagesModel."""

    #     verbose_name = 'PagesModel'
    #     verbose_name_plural = 'PagesModels'

    def __str__(self):
        """Unicode representation of PagesModel."""
        
        return self.name

