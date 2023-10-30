from django import forms

def passwordvalidator(value):
    if len(value)<8:
        raise forms.ValidationError("Password must contain atleast 8 characters")
    
class EnrollmentForm(forms.Form):
    name=forms.CharField(error_messages={'required':"please enter your name"},widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(error_messages={'required':'please enter your valid email address'},widget=forms.EmailInput(attrs={'class':'form-control'}))
    password=forms.CharField(validators=[passwordvalidator],widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(validators=[passwordvalidator],label="Confirm password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    def clean(self):
        cleaned_data=super().clean()
        password1=cleaned_data.get('password')
        password2=cleaned_data.get('password2')
        if password1!=password2:
            raise forms.ValidationError("Password does not match ! ")