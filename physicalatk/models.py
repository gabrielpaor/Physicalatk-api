from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=6, blank=True, null=True ,choices=GENDER_CHOICES)