from django import forms
from .models import Student

class EnrollForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),
                 'email':forms.EmailInput(attrs={'class':'form-control'}),
                 'pin':forms.TextInput(attrs={'class':'form-control'})}