from django import forms 
from .models import Student

def namevalidator(value):
    if len(value)<5:
        raise forms.ValidationError("must contain 5 character atleast.")
    for c in value:
        if c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ":
            raise forms.ValidationError("name must contain string only.")
def contactvalidator(value):
    for c in value:
        if c not in '1234567890':
            raise forms.ValidationError("must be number only ! ")
    if len(value)>10:
        raise forms.ValidationError("contact must be of 10 digit only ")
    
class EnrollmentForm(forms.ModelForm):
    name=forms.CharField(validators=[namevalidator],error_messages={'required':'please enter name'},max_length=40,widget=forms.TextInput(attrs={'class':'form-control'}))
    contact=forms.CharField(validators=[contactvalidator],error_messages={'required':'please enter contact number'},max_length=10,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=Student
        fields=['name','email','contact']
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),
                 'email':forms.EmailInput(attrs={'class':'form-control'}),
                 'contact':forms.TextInput(attrs={'class':'form-control'})}
        error_messages={'name':{'required':'please enter student name'},
                        'email':{'required':'please enter student email address'},
                        'contact':{'required':'please enter contact number'}}
        
    def clean(self):
        cleaned_data=super().clean()
        email=cleaned_data.get('email')
        emails=Student.objects.filter(email=email)
        if emails:
            raise forms.ValidationError("email already exist")