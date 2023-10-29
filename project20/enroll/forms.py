from django import forms

class EnrollForm(forms.Form):
    name=forms.CharField(label="Name",label_suffix=" ",widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(label="E-mail",label_suffix=" ",widget=forms.EmailInput(attrs={'class':'form-control'}))
    password=forms.CharField(label="Password",label_suffix=" ",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    cpassword=forms.CharField(label="Password again",label_suffix=" ",widget=forms.PasswordInput(attrs={'class':'form-control'}))