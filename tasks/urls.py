from django.conf.urls import patterns, url
from .views import set_proj_view, task_detail, task_typed_print, task_detail_print, set_task_done
from .views import taskprojview, get_task_pdf, proj_tree, testjs, taskmain, taskmain_projview, proj_tasks_sidebar
from .views import new_task
urlpatterns = patterns('',
                       url(r'^new/(?P<parent_id>\d+)/(?P<tree_id>\d+)$', new_task, name='new_task'),
                       # url(r'^edit/(?P<task_id>\d+)$', 'task.views.edit_task', name='edit_task'),
                       url(r'^view/$', taskprojview, {'done': False}, name='proj_tasks'),
                       url(r'^view/done/$', taskprojview, {'done': True}, name='proj_tasks_done'),
                       # switching to Ajax fills by jquery for tasks
                       url(r'^main/$', taskmain, name='tasks_main'),
                       url(r'^main/open/$', taskmain_projview, {'done': False, 'tree_id': 1}, name='proj_tasks_jq'),
                       url(r'^main/done/(?P<tree_id>\d+)/(?P<done>\w+)$', taskmain_projview,name='proj_tasks_done_jq'),
                       url(r'^main/open/(?P<tree_id>\d+)/$', taskmain_projview, name='proj_tasks_tree_jq'),
                       url(r'^main/sitebar/(?P<tree_id>\d+)/$', proj_tasks_sidebar, name='proj_tasks_sitebar'),
                       # switching to Ajax end
                       url(r'^project-tree/$', proj_tree, {'template': 'tasks/proj_tree.html'}, name='proj_tree'),
                       url(r'^project-tree-jq/$', proj_tree,
                           {'template': 'tasks/proj_tree_jq.html'}, name='proj_tree_jq'),
                       url(r'^view/(?P<proj_id>\d+)$', set_proj_view, name='task_set_view'),
                       url(r'^testjs/$', testjs, name='testjs'),
                       url(r'^(?P<task_id>\d+)/$', task_detail, name='detail_task'),
                       url(r'^print/(?P<task_id>\d+)/$', task_detail_print, name='print_detail_task'),
                       url(r'^Tprint/(?P<task_id>\d+)/$', task_typed_print, name='print_typed_task'),
                       # for PDF
                       url(r'^PDFtask/(?P<task_id>\d+)/$', get_task_pdf, name='get_task_pdf'),
                       # ---
                       url(r'^done/(?P<task_id>\d+)/$', set_task_done, name='done_task'),
                       )
