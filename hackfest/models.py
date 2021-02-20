from django.db import models

# Create your models here.
class Donor(models.Model):
    GENDER=(
        ('M', 'male'),
        ('F', 'female'),
        ('O', 'other'),
    )

    BLOOD_GROUP=(
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),

    
    )

    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    gender= models.CharField(max_length=1, null=True, choices=GENDER)
    contact= models.CharField(max_length=15)
    dob= models.DateField(null=True)
    blood= models.CharField(max_length=200, null=True, choices=BLOOD_GROUP)
    district= models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    ward= models.IntegerField(null=True)

    def __str__(self):
        return self.first_name



class BloodBank(models.Model):
    name= models.CharField(max_length=50, null=True)
    address= models.CharField(max_length=50, null=True)
    city= models.CharField(max_length=50, null=True)
    contact= models.CharField(max_length=15, null=True)
    email= models.EmailField(null=True)
    website= models.CharField(max_length=50)
    image= models.ImageField(upload_to= 'images')
   


    def __str__(self):
        return self.name