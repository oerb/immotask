__author__ = 'leppin'

from django.conf.urls import patterns, url
from .views import project_choice, project_new

urlpatterns = patterns('',
                       url(r'^choice/$', project_choice, name='proj_choice' ),
                       url(r'^new/$', project_new, name='proj_new' ),
                       )