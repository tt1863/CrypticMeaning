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
    
class Thread(models.Model):
    forum = models.ForeignKey(Forum)
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField('date created')
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.title
    
class Post(models.Model):
    thread = models.ForeignKey(Thread)
    content = models.CharField(max_length=5000)
    date_posted = models.DateTimeField('date posted')
    
    def __unicode__(self):
        return self.content
