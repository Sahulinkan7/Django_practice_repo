from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import ( UserCreationForm,UserChangeForm,AuthenticationForm,
                                    PasswordChangeForm,SetPasswordForm ) 

class SignupForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label="confirm password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','password']
        

class UserprofileForm(UserChangeForm):
    password=None
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    date_joined=forms.CharField(disabled=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_login=forms.CharField(disabled=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined','last_login']
        



class ChangePasswordForm(PasswordChangeForm):
    old_password=forms.CharField(label="Old password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1=forms.CharField(label="New password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2=forms.CharField(label="New password confirmation",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User 
        fields="__all__"
        
        
class SetnewpasswordForm(SetPasswordForm):
    new_password1=forms.CharField(label="new passsword",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2=forms.CharField(label="new password confirmation",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields="__all__"
        
