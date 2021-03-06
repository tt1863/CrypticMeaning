from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone


class Forum(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    sequence = models.IntegerField()
    
    def __unicode__(self):
        return self.title
    
    def last_post(self):
        threads = Thread.objects.filter(forum=self)
        last_post = Post.objects.filter(thread=threads).latest('date_posted').date_posted
        
        if last_post:
            return last_post
        else:
            return "None"
    
    def num_threads(self):
        return Thread.objects.filter(forum=self).count()
    
    def num_posts(self):
        return Post.objects.filter(thread=Thread.objects.filter(forum=self)).count()
        
    
class Thread(models.Model):
    forum = models.ForeignKey(Forum)
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField('date created')
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.title
    
    def last_post(self):
        last_post = Post.objects.filter(thread=self).latest('date_posted').date_posted
        return last_post
    
    def num_replies(self):
        num_posts = Post.objects.filter(thread=self).count()
        if num_posts >= 1:
            return num_posts - 1
        else:
            return num_posts
    
    
class Post(models.Model):
    thread = models.ForeignKey(Thread)
    content = models.CharField(max_length=5000)
    date_posted = models.DateTimeField('date posted')
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.content
    
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='avatars', blank=True)
    birthday = models.DateField(blank=True)
    
    def __unicode__(self):
        return self.user.username
    
    def profile_url(self):
        return "/forums/profile/" + self.user.username
    
