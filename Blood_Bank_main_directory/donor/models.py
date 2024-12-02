from django.db import models

# Create your models here.

class Donor(models.Model):
    GENDER_CHOICES = [
        ('MALE','male'),
        ('FEMALE','female'),
        ('TRANSGENDER', 'transgender'),
    ]
    BLOOD_GROUP_CHOICES = [
        ('A-POSITIVE', 'A+'),
        ('A-NEGATIVE', 'A-'),
        ('B-POSITIVE','B+'),
        ('B-NEGATIVE','B-'),
        ('AB-POSTITVE','AB+'),
        ('AB-NEGATIVE','AB-'),
        ('O-POSITIVE','O+'),
        ('O-NEGATIVE','O-'),
    ]
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=50,choices=GENDER_CHOICES)
    #blood_group, Contact, CNIC, Address
    blood_group = models.CharField(max_length=50,choices=BLOOD_GROUP_CHOICES)
    contact = models.PositiveSmallIntegerField("Enter your phone number, 11 digits only.")
    cnic = models.PositiveSmallIntegerField("Enter your CNIC.")
    address = models.TextField()
    
    
    def __str__(self):
        return self.name