from django import forms
from .models import StudentModel
class EnrollmentForm(forms.Form):
    name=forms.CharField(error_messages={'required':'please enter your name'},widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(error_messages={'required':'please enter your email address'},widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    cpassword=forms.CharField(label="Confirm password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    def clean(self):
        cleaned_data=super().clean()
        email=cleaned_data.get("email")
        pass1=cleaned_data.get('password')
        pass2=cleaned_data.get('cpassword')
        if pass1!=pass2:
            raise forms.ValidationError("password not matched !")
        emails=StudentModel.objects.filter(email=email)
        print(emails)
        if len(emails):
            raise forms.ValidationError("email already exist ! ")
        