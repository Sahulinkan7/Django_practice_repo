from django.db import models

# Create your models here.
class Examcenter(models.Model):
    name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    
    
class Student(Examcenter):
    sname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    
    