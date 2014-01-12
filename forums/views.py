from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from forums.models import Forum, Thread, Post
#from forums.forms import CategoryForm, PageForm, UserForm, UserProfileForm
from datetime import datetime
import urllib2

def index(request):
    context = RequestContext(request)
    forum_list = Forum.objects.order_by("sequence")
    
    for forum in forum_list:
        forum.url = urlencode(forum.title)
    
    context_dict = {'forum_list': forum_list}
    return render_to_response('forums/index.html', context_dict, context)

@login_required
def forum(request, forum_title_url):
    context = RequestContext(request)
    
    forum_title = urldecode(forum_title_url)
    
    context_dict = {'forum_title': forum_title,
                    'forum_title_url': forum_title_url}
    
    try:
        forum = Forum.objects.get(title=forum_title)
        
        threads = Thread.objects.filter(forum=forum)
        
        for thread in threads:
            thread.url = encode_url(thread.title)
        
        context_dict['forum'] = forum
        context_dict['threads'] = threads
    except Forum.DoesNotExist:
        pass
    
    return render_to_response('forums/forum.html', context_dict, context)

@login_required
def thread(request, forum_title_url, thread_title_url):
    context = RequestContext(request)
    
    forum_title = decode_url(forum_title_url)
    thread_title = decode_url(thread_title_url)
    
    context_dict = {'thread_title': thread_title,
                    'thread_title_url': thread_title_url}
    
    try:
        forum = Forum.objects.get(title=forum_title)
        thread = Thread.objects.get(forum=forum, title=thread_title)
        
        posts = Post.objects.filter(thread=thread).order_by('-date_posted')
        
        context_dict['thread'] = thread
        context_dict['posts'] = posts
    except Thread.DoesNotExist:
        pass
    
    return render_to_response('forums/thread.html', context_dict, context)

def user_login(request):
    # Like before, obtain the context for the user's request
    context = RequestContext(request)
    
    success = True
    
    # If the request is a HTTP POST, try to pull out the relevant information
    if request.method == 'POST':
        # Gather the username and password provided by the user
        # This information is obtained from the login form
        username = request.POST['username']
        password = request.POST['password']
        
        # User Django's machinery to attemp to see if the username/password
        # combination is valid - a User object is returned if it is
        user = authenticate(username=username, password=password)
        
        # If we have a User object, the details are correct
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found
        if user is not None:
            # is the account active? It could have been disabled
            if user.is_active:
                # If the account is valid and active, we can log the user in
                login(request, user)
                return HttpResponseRedirect('/forums')
            else:
                # An inactive account was used - no logging in!
                success = False
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    
    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('forums/login.html', {}, context)
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/forums')

def decode_url(forum_title_url):
    forum_title = forum_title_url.replace('_', ' ')
    return forum_title

def encode_url(forum_title):
    forum_title_url = forum_title.replace(' ', '_')
    return forum_title_url

def urlencode(s):
    s = s.replace(' ', '_')
    return urllib2.quote(s)
 
def urldecode(s):
    s = s.replace('_', ' ')
    return urllib2.unquote(s).decode('utf8')

