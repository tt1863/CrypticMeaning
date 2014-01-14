from django.conf.urls import patterns, include, url
from forums import views

urlpatterns = patterns('',
    # ex: /forums
    url(r'^$', views.index, name='index'),
    # ex: /forums/login
    url(r'^login/', views.user_login, name='login'),
    # ex: /forums/logout
    url(r'^logout/', views.user_logout, name='logout'),
    # ex: /forums/General Forum/create_thread
    url(r'^(?P<forum_title_url>\w+)/create_thread/$', views.create_thread, name='create_thread'),
    # ex: /forums/General_Forum/
    url(r'^(?P<forum_title_url>\w+)/$', views.forum, name='forum'),
    
    # ex: /forums/General_Forum/My_first_thread
    url(r'^(?P<forum_title_url>\w+)/(?P<thread_title_url>\w+)', views.thread, name='thread'),
    
)