from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms 

class SignupForm(UserCreationForm):
    password1=forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label="Confirm password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(error_messages={'required':'please enter first name'},widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(error_messages={'required':'please enter last name'},widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(error_messages={'required':'please enter email id'},widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'E-mail'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}
        error_messages={'username':{'required':'please enter your username'}}
        