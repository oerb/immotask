__author__ = 'leppin'

from django.conf.urls import patterns, url
from .views import project_choice, project_new, project_edit, all_projects, new_proj_contact_type, proj_edit_adrtype

urlpatterns = patterns('',
                       url(r'^choice/$', project_choice, name='proj_choice' ),
                       url(r'^new/$', project_new, name='proj_new' ),
                       url(r'^edit/(?P<proj_id>\d+)$', project_edit, name='proj_edit' ),
                       url(r'^view/$', all_projects, name='proj_all' ),
                       url(r'^view/(?P<proj_id>\d+)/(?P<hide>\d+)$', 'projects.views.project_set_view',
                           name='proj_set_view'),
                       url(r'^new_adrtype/$', new_proj_contact_type, name='proj_new_adrtype' ),
                       url(r'^edit_adrtype/(?P<projadrtype_id>\d+)$', proj_edit_adrtype, name='proj_edit_adrtype' ),
                       )