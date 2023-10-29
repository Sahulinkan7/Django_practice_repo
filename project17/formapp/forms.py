from django import forms

class RegistrationForm(forms.Form):
    name=forms.CharField(help_text="enter your name")
    email=forms.EmailField()
    address=forms.CharField()