from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

class Shout(models.Model):
    content = models.CharField(max_length=1000)
    date = models.DateField()
    user = models.ForeignKey(User)
