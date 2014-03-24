__author__ = 'leppin'

from django.conf.urls import patterns, url
from .views import project_choice

urlpatterns = patterns('',
                       url(r'^choice/$', project_choice, name='proj_choice' ),
                       )