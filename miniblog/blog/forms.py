from django import forms 

from .models import Post

class BlogForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    desc=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model=Post
        fields=['title','desc']