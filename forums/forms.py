from django import forms
from forums.models import Thread, Post
from django.contrib.auth.models import User
from django.forms import Textarea
from datetime import datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ThreadForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    
    def __init__(self, *args, **kwargs):
        super(ThreadForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_id = 'thread_form'
        self.helper.form_class = 'form'
        self.helper.form_method = 'post'
    
    class Meta:
        model = Thread
        fields = ('title',)
        exclude = ('forum', 'date_created', 'user')
        
        
class PostForm(forms.ModelForm):
    content = forms.CharField(max_length=5000, widget=forms.Textarea)
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_action = '/forums/{{ forum_url }}/create_thread/'
        self.helper.add_input(Submit('submit', 'Submit'))
    
    class Meta:
        model = Post
        fields = ('content',)
        exclude = ('thread', 'date_posted')