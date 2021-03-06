from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CrypticMeaning.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', include('forums.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^forums/', include('forums.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
)

urlpatterns += staticfiles_urlpatterns()