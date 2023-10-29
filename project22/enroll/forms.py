from django import forms

class EnrollForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(min_length=10,max_length=100,widget=forms.EmailInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label="password again",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    def clean_name(self):
        name=self.cleaned_data['name']
        for c in name:
            if c in '!@#$%^&*(){}[]-/|<>?' :
                raise forms.ValidationError("name should not contain special characters")
        else:
            return name