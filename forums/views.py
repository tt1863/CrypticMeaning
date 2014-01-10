from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
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

def thread(request, forum_title_url, thread_title_url):
    context = RequestContext(request)
    
    forum_title = decode_url(forum_title_url)
    thread_title = decode_url(thread_title_url)
    
    context_dict = {'thread_title': thread_title,
                    'thread_title_url': thread_title_url}
    
    try:
        forum = Forum.objects.get(title=forum_title)
        thread = Thread.objects.get(forum=forum, title=thread_title)
        
        posts = Post.objects.filter(thread=thread)
        
        context_dict['thread'] = thread
        context_dict['posts'] = posts
    except Thread.DoesNotExist:
        pass
    
    return render_to_response('forums/thread.html', context_dict, context)

def user_login(request):
    context = RequestContext(request)
    return render_to_response('forums/login.html', {}, context)

def view_forum(request):
    return "Forum view"

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

