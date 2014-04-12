from django.conf.urls import patterns, url
from .views import set_proj_view, task_detail, task_typed_print, task_detail_print, set_task_done
from .views import taskprojview, get_task_pdf
urlpatterns = patterns('',
                       url(r'^new/(?P<parent_id>\d+)$', 'tasks.views.new_task', name='new_task'),
                       # url(r'^edit/(?P<task_id>\d+)$', 'task.views.edit_task', name='edit_task'),
                       url(r'^view/$', taskprojview, {'done': False}, name='proj_tasks'),
                       url(r'^view/done/$', taskprojview, {'done': True}, name='proj_tasks_done'),
                       url(r'^view/(?P<proj_id>\d+)$', set_proj_view, name='task_set_view'),
                       url(r'^(?P<task_id>\d+)/$', task_detail, name='detail_task'),
                       url(r'^print/(?P<task_id>\d+)/$', task_detail_print, name='print_detail_task'),
                       url(r'^Tprint/(?P<task_id>\d+)/$', task_typed_print, name='print_typed_task'),
                       # for PDF
                       url(r'^PDFtask/(?P<task_id>\d+)/$', get_task_pdf, name='get_task_pdf'),
                       # ---
                       url(r'^done/(?P<task_id>\d+)/$', set_task_done, name='done_task'),
                       )
