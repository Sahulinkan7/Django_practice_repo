from django import forms
from .models import StudentModel

class EnrollmentForm(forms.ModelForm):
    password2=forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=StudentModel
        fields=['name','email','password']
        help_texts={'name':'enter your full name'}
        labels={'name':'Name','email':'E-mail'}
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),
                 'email':forms.EmailInput(attrs={'class':'form-control'}),
                 'password':forms.PasswordInput(attrs={'class':'form-control'})}
        error_messages={'name':{'required':'please enter your name'},
                        'email':{'required':'please enter your email'}}
        
        
    def clean(self):
            cleaned_data=super().clean()
            password1=cleaned_data.get('password')
            password2=cleaned_data.get('password2')
            print(password1,password2)
            if password1!=password2:
                raise forms.ValidationError("password is not matching ! ")