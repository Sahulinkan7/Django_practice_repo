from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label="confirm password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email=forms.CharField(label="Email",widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}
        
class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields="__all__"
        
class PasswordnewForm(PasswordChangeForm):
    old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields="__all__"
        

class Setuserpassword(SetPasswordForm):
    new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields="__all__"