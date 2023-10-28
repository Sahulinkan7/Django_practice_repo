from django.db import models

# Create your models here.
class Student(models.Model):
    stuid=models.IntegerField()
    stuname=models.CharField(max_length=100)
    stuemail=models.EmailField(max_length=100)
    stubgrp=models.CharField(max_length=10,default="Not available")
    