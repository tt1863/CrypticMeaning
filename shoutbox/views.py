from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from shoutbox.models import Shout
from datetime import datetime


def index(request):
    context = RequestContext(request)
    
    shouts = Shout.objects.order_by('-date')[:30]
    
    context_dict = {'shouts': shouts}
    
    return render_to_response('shoutbox/index.html', context_dict, context)