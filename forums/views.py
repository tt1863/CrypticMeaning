from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from forums.models import Forum, Thread, Post
from forums.forms import ThreadForm, PostForm
from datetime import datetime
import urllib2

def index(request):
    context = RequestContext(request)
    forum_list = Forum.objects.order_by("sequence")
    
    for forum in forum_list:
        forum.url = slugify(forum.title) + "-" + str(forum.id)
    
    context_dict = {'forum_list': forum_list}
    return render_to_response('forums/index.html', context_dict, context)

@login_required
def forum(request, forum_slug, forum_id):
    context = RequestContext(request)
    
    try:
        forum = Forum.objects.get(id=forum_id)
        
        threads = Thread.objects.filter(forum=forum)
        
        for thread in threads:
            thread.url = slugify(thread.title) + "-" + str(thread.id)
            
        forum.url = forum_slug + "-" + str(forum.id)
            
        context_dict = {'forum': forum,
                        'threads': threads}
        
    except Forum.DoesNotExist:
        pass
    
    return render_to_response('forums/forum.html', context_dict, context)

@login_required
def thread(request, forum_slug, forum_id, thread_slug, thread_id):
    context = RequestContext(request)
    
    try:
        thread = Thread.objects.get(id=thread_id)
        
        posts = Post.objects.filter(thread=thread)
        
        thread.url = thread_slug + "-" + str(thread_id)
        forum_url = forum_slug + "-" + str(thread_id)
        
        context_dict = {'thread': thread,
                        'posts': posts,
                        'forum_url': forum_url}
        
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
    
def create_thread(request, forum_slug, forum_id):
    context = RequestContext(request)
    
    forum_object = Forum.objects.get(id=forum_id)
    forum.url = forum_slug + "-" + str(forum_object.id)
    
    if request.method == 'POST':
        thread_form = ThreadForm(request.POST)
        post_form = PostForm(request.POST)
        
        if thread_form.is_valid() and post_form.is_valid():
            
            thread_object = thread_form.save(commit=False)
            post = post_form.save(commit=False)
        
            user = User.objects.get(username=request.user)
            date = datetime.now()
            
            thread_object.forum = forum_object
            thread_object.date_created = date
            thread_object.user = user
            
            thread_object.save()
            
            post.thread = thread_object
            post.user = user
            post.date_posted = date
            
            post.save()
            
            thread_slug = slugify(thread_object.title)
            thread_id = thread_object.id
            
            #return forum(request, forum_slug, forum_id)
            return thread(request, forum_slug, forum_id, thread_slug, thread_id)
        else:
            print thread_form.errors, post_form.errors
    else:
        thread_form = ThreadForm()
        post_form = PostForm()
        
    context_dict = {'thread_form': thread_form,
                    'post_form': post_form,
                    'forum_url': forum.url}
        
    return render_to_response('forums/create_thread.html', context_dict, context)
    
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

