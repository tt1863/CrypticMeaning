from django.conf.urls import patterns, include, url
from forums import views

urlpatterns = patterns('',
    # ex: /forums/
    url(r'^$', views.index, name='index'),
    # ex: /forums/General_Forum/
    url(r'^(?P<forum_title_url>\w+)/$', views.forum, name='forum'),
    # ex: /forums/General_Forum/My_first_thread
    url(r'^(?P<forum_title_url>\w+)/(?P<thread_title_url>\w+)', views.thread, name='thread'),
)