from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from app_key.views import hello
from django.conf.urls.defaults import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djan.views.home', name='home'),
    # url(r'^djan/', include('djan.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    ('^hello/$', hello),
)
