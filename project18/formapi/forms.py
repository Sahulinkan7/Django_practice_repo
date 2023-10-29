from django import forms
import datetime
class RegistrationForm(forms.Form):
    name=forms.CharField(disabled=True,initial="abcd",label="Name",label_suffix=" ")
    email=forms.EmailField(initial="abc@sds.com",help_text="enter your personal email id only",label="E-mail")
    pin=forms.CharField(help_text="pin must be 6 digit only",initial=999898)
    age=forms.IntegerField(help_text="age must be integer only",initial=18)
    time=forms.DateTimeField(initial=datetime.datetime.now)