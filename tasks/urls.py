from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^new/$', 'tasks.views.new_task', name='new_task'),
                       # url(r'^edit/(?P<task_id>\d+)$', 'task.views.edit_task', name='edit_task'),
                       url(r'^view/$', 'tasks.views.taskprojview', name='proj_tasks'),
                       url(r'^(?P<task_id>\d+)/$', 'tasks.views.task_detail', name='detail_task'),
                       url(r'^print/(?P<task_id>\d+)/$', 'tasks.views.task_detail_print', name='print_detail_task'),
                       url(r'^Tprint/(?P<task_id>\d+)/(?P<tasktype_id>\d+)/$', 'tasks.views.task_typed_print', name='print_typed_task'),
)
