from django import forms 
from .models import Student


class MyForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','email','course']
        widgets= {'name':forms.TextInput(attrs={'class':'form-control'}),
                  'email':forms.TextInput(attrs={'class':'form-control'}),
                  'course':forms.TextInput(attrs={'class':'form-control'})}