from django import forms

class StudentRegistration(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    school_name=forms.CharField()