# from django.views.generic import TemplateView
from django.views.generic import ListView
from django.conf.urls.defaults import *
from django.contrib import admin
from artsite.models import Festival
admin.autodiscover()

urlpatterns = patterns( '',
    ( r'^festivals/$', ListView.as_view( model = Festival ) ),
    ( r'^admin/doc/', include( 'django.contrib.admindocs.urls' ) ),
    ( r'^admin/doc/', include( 'django.contrib.admindocs.urls' ) ),
    ( r'^admin/', include( admin.site.urls ) ),
  )
