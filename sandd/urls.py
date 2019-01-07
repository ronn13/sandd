from django.conf.urls import include, url
from django.contrib import admin
from adm.views import *

admin.autodiscover()

urlpatterns = [
    url(r'^$', index, name='index'),
    #change regex below to accept 1 or more of number as product id
    url(r'^products/(?P<pdt_id>[0-9]?)/$', pdt_page, name='pdt_page'),
    url(r'^(?P<region>[A-Z][a-z]+)/$', store_totals, name='store_totals'),
    url(r'^(?P<region>[A-Z][a-z]+)/(?P<store_id>[0-9]+)/$', store_profile, name='store_profile'),
	
    url(r'^agent_form/', agent_form, name='agent_form'),
    url(r'^store_admin/', store_admin, name='store_admin'),
    url(r'^agent_admin/', agent_admin, name='agent_admin'),
    url(r'^location_admin/', location_admin, name='location_admin'),
    url(r'^region_admin/', region_admin, name='region_admin'),
    
    url(r'^(?P<agent>[a-z]+[0-9]+)/$', agent_profile, name='agent_profile'),

    url(r'^admin/', admin.site.urls),
]
