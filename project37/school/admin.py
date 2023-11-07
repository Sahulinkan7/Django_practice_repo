from django.contrib import admin
from .models import Student,Teacher

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','email','dob','fees','course']
    
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=['id','name','email','dob','salary']
