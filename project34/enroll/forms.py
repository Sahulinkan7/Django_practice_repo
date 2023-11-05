from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms 

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields="__all__"
        
class SignupForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']
        
        
class EdituserForm(UserChangeForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    date_joined=forms.CharField(disabled=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_login=forms.CharField(disabled=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined','last_login']
        
class EditformForAdmin(UserChangeForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    date_joined=forms.CharField(disabled=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_login=forms.CharField(disabled=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    password=None
    class Meta:
        model=User 
        fields=['username','first_name','last_name','email','date_joined','last_login','is_staff','is_active']