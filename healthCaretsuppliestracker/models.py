from django.db import models

# Create your models here.


class Donor(models.Model):
    name = models.CharField(max_length=30, default='no name')
    email = models.EmailField(max_length=60, default=0)
    phone_number = models.IntegerField(default=0)
    location = models.CharField(max_length=60, default='no location')
