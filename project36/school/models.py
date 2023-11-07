from django.db import models

# Create your models here.

class Students(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    roll=models.IntegerField()
    city=models.CharField(max_length=255)
    marks=models.IntegerField()
    admdatetime=models.DateTimeField()
    passdatetime=models.DateField()
