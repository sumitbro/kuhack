from django.db import models

# Create your models here.
class Donor(models.Model):
    CHOOSE=(
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other'),
    )

    GROUP=(
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B-'),
        ('O+', 'O-'),
        ('AB+', 'AB-'),
    
    )

    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    gender= models.CharField(max_length=200, null=True, choices=CHOOSE)
    contact= models.CharField(max_length=50000000000)
    dob= models.DateField(null=True)
    blood= models.CharField(max_length=200, null=True, choices=GROUP)
    district= models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    ward= models.IntegerField(null=True)

    def __str__(self):
        return self.first_name