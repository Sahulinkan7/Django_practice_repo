from django import forms

def passwordvalidator(value):
    if value[0]!='P':
        raise forms.ValidationError("password must startwith P")
            
class EnrollmentForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password=forms.CharField(validators=[passwordvalidator],widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    def clean(self):
        cleaned_data=super().clean()
        name=cleaned_data.get('name')
        pass1=cleaned_data.get('password')
        pass2=cleaned_data.get('password2')
        if pass1 != pass2:
            raise forms.ValidationError("password not matched !")
        if name[0]!='S':
            raise forms.ValidationError("name must start with S")
        