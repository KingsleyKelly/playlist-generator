from django.conf import settings
from django.conf.urls.defaults import *
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('todo.views',
    url(r'^/?$', 'index', name='index'),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)
