from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length=255)
    phone_number = PhoneNumberField()
    image = models.ImageField(upload_to='files/images/',null=True,blank=True)
    email = models.EmailField(max_length=200, unique=True, null=True, blank=True)
    age = models.IntegerField( null=True, blank=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    address = models.TextField(max_length=250, null=True, blank=True)
    #fax_number = PhoneNumberField(blank=True)

class qualification(models.Model):
    course=models.CharField(max_length=200)
    university=models.CharField(max_length=200)
    year=models.DateField()
    percentage=models.IntegerField()