from django.db import models

# Create your models here.
class CommoInfo(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    dob=models.DateField()
    class Meta:
        abstract=True
    
class Student(CommoInfo):
    fees=models.IntegerField()
    course=models.CharField(max_length=100)
    
class Teacher(CommoInfo):
    salary=models.IntegerField()