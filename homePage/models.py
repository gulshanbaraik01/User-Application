from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.

class Employee(models.Model):
    empname=models.CharField(max_length=100)
    age=models.CharField(max_length=10)
    gender=models.CharField(max_length=10)
    qualification=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    pincode=models.CharField(max_length=10)
    employment=models.CharField(max_length=20)
    password=models.CharField(max_length=50)
    usertype=models.CharField(max_length=50)

    
    
    def __str__(self):
        return self.empname
