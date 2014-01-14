from django import forms
from forums.models import Thread, Post
from django.contrib.auth.models import User
from datetime import datetime

class ThreadForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    
    class Meta:
        model = Thread
        fields = ('title',)
        exclude = ('forum', 'date_created', 'user')
        
class PostForm(forms.ModelForm):
    content = forms.CharField(max_length=5000)
    
    class Meta:
        model = Post
        fields = ('content',)
        exclude = ('thread', 'date_posted')