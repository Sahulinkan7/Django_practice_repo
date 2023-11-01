from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    password1=forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class':'form-control mt-1'}))
    password2=forms.CharField(label="confirm password",widget=forms.PasswordInput(attrs={'class':'form-control mt-1'}))
    email=forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'class':'form-control mt-1'}))
    first_name=forms.CharField(label="First name",widget=forms.TextInput(attrs={'class':'form-control mt-1'}))
    last_name=forms.CharField(label="Lat name",widget=forms.TextInput(attrs={'class':'form-control mt-1'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        widgets={'username':forms.TextInput(attrs={'class':'form-control mt-1'})}
        
        
class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields="__all__"