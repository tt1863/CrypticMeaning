from django.conf.urls import patterns, include, url
from forums import views

urlpatterns = patterns('',
    # ex: /forums
    url(r'^$', views.index, name='index'),
    # ex: /forums/login
    #url(r'^login/', views.user_login, name='login'),
    # ex: /forums/logout
    url(r'^logout/', views.user_logout, name='logout'),
    
    # ex: /forums/General Forum/create_thread
    url(r'^(?P<forum_slug>[-\w\d]+)-(?P<forum_id>\d+)/create_thread/$', views.create_thread, name='create_thread'),
    
    # ex: /forums/general_forum-1
    url(r'^(?P<forum_slug>[-\w\d]+)-(?P<forum_id>\d+)/$', views.forum, name='forum'),
    
    # ex: /forums/general_forum-1/my_first_thread-1
    url(r'^(?P<forum_slug>[-\w\d]+)-(?P<forum_id>\d+)/(?P<thread_slug>[-\w\d]+)-(?P<thread_id>\d+)/$', views.thread, name='thread'),
    
    # ex: /forums/general_form-1/my_first_thread-1/reply
    url(r'^(?P<forum_slug>[-\w\d]+)-(?P<forum_id>\d+)/(?P<thread_slug>[-\w\d]+)-(?P<thread_id>\d+)/reply/$', views.reply, name='reply'),
    
    # ex: /forums/General_Forum/
    #url(r'^(?P<forum_title_url>\w+)/$', views.forum, name='forum'),
    
    # ex: /forums/General_Forum/My_first_thread
    #url(r'^(?P<forum_title_url>\w+)/(?P<thread_title_url>\w+)', views.thread, name='thread'),
    
)