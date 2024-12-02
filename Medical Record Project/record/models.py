from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Patient(models.Model):
    #todo
    #patient_name, address, phone number, doctor attending, history, remarks/diagnosis, prescribed medicine
    MALE = 'MA'
    FEMALE = 'FMA'
    TRANSGENDER = 'TG'
    GENDER_CHOICES = [(MALE,'Male'),(FEMALE, 'Female'),(TRANSGENDER,'Transgender'),]
    
    
    patient_name = models.CharField(max_length=255)
    gender = models.TextField(max_length=3,choices=GENDER_CHOICES,default=MALE)
    age = models.IntegerField(default=18)
    date_of_checkup=models.DateField( default=timezone.now())
    doctor_attending = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    address = models.TextField()
    presenting_complaint=models.CharField(max_length=255)
    history_of_presenting_complaint=models.TextField()
    systemic_inquiry=models.TextField()#text field
    past_medical_history=models.CharField( max_length=50)
    past_surgical_history=models.CharField("Past Surgical History", max_length=50)
    drug_history=models.CharField("Drug History", max_length=255)
    allergies=models.CharField("Allergies", max_length=50)
    travel_history=models.CharField("Travel History", max_length=255)
    blood_transfusion_history=models.CharField(default=None, max_length=50)
    sexual_history=models.CharField(default=None, max_length=50)
    cns_examination=models.CharField(max_length=255)
    general_physical_examination=models.CharField( max_length=255)
    
    higher_mental_functions=models.TextField()
    cranial_nerves = models.TextField('Cranial Nerves')
    motor_system=models.TextField("Motor System")
    sensory_system=models.TextField("sensory System")
    cerebellum=models.CharField(max_length=255)
    somi=models.CharField(max_length=255)
    gait=models.CharField(max_length=255)
    back_tenderness = models.CharField(max_length=255)
    
    def __str__(self):
        return self.patient_name
    
    def get_absolute_url(self):
        return reverse('patient_detail', args=[str(self.id)])