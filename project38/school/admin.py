from django.contrib import admin
from .models import Student,Examcenter

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','sname','email','name','city']
    
@admin.register(Examcenter)
class ExamcenterAdmin(admin.ModelAdmin):
    list_display=['id','name','city']
