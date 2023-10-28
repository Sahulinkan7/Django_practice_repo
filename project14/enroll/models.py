from django.db import models

# Create your models here.
class Student(models.Model):
    stuid=models.IntegerField()
    stuemail=models.EmailField(max_length=100)
    stuname=models.CharField(max_length=100)
    stupass=models.CharField(max_length=100)
