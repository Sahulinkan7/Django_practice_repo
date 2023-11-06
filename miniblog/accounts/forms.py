from django import forms 

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

# signup form
class SignupForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label="Password confirmation",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']
    def clean(self):
        cleaned_data=super().clean()
        username=cleaned_data.get('username')
        if username is not None:
            if username[0] in '1234567890':
                raise forms.ValidationError("username must start with a character")
            
class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields="__all__"
        
        