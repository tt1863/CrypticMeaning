from django import forms
from forums.models import Thread, Post
from django.contrib.auth.models import User

class ThreadForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    user = forms.CharField(widget=forms.HiddenInput())
    
    class Meta:
        model = Thread
        fields = ('title',)
        
class PostForm(forms.ModelForm):
    content = forms.CharField(max_length=5000)
    
    class Meta:
        model = Post