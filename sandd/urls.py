from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sandd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
"""sandd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from adm.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    #change regex below to accept 1 or more of number as product id
    url(r'^products/(?P<pdt_id>[0-9]+)/$', pdt_page, name='pdt_page'),
    url(r'^(?P<region>[A-Z][a-z]+)/$', store_totals, name='store_totals'),
    url(r'^(?P<region>[A-Z][a-z]+)/(?P<store_id>[0-9]+)/$', store_profile, name='store_profile'),
	
    url(r'^agent_form/', agent_form, name='agent_form'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<agent>[a-z]+)/$', agent_profile, name='agent_profile'),
]
