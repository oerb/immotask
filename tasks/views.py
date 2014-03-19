from django.shortcuts import render, get_object_or_404, redirect
from tasks.models import Task, TaskType, TaskDoc, AuthoriseStruct
from tasks.forms import TaskForm
from usrsettings.models import Setting
from projects.models import ProjTask
from django.shortcuts import get_object_or_404, render, redirect
from contacts.models import ContactData

# Create your views here.
def new_task(request):
    message = None
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task(ta_shorttxt=form.cleaned_data['shorttxt'],
                        ta_longtxt=form.cleaned_data['longtxt'],
                        ta_begin=form.cleaned_data['begin'],
                        ta_begintime=form.cleaned_data['begintime'],
                        ta_end=form.cleaned_data['end'],
                        ta_endtime=form.cleaned_data['endtime'],
                        ta_warn=form.cleaned_data['warn'],
                        ta_editor=request.user,
                        ta_priority=form.cleaned_data['priority'],
                        ta_adrid_from=form.cleaned_data['adr_from'],
                        ta_adrid_to=form.cleaned_data['adr_to'],
                        ta_tasktype=form.cleaned_data['tasktype'],
                        )
            task.save()
            usersetting = Setting.objects.filter(se_user=request.user)
            if usersetting:
                for pid in usersetting:
                    proj_id = pid.se_current_proj
                    projtask = ProjTask(pt_taskid=task, pt_projid=proj_id)
                    projtask.save()

            return redirect('proj_contacts')
    else:
        form = TaskForm()
    return render(request, 'contacts/new_contact.html', {'message': message, 'form': form})


def taskprojview(request):
    if request.user.is_authenticated():
        current_proj = Setting.objects.filter(se_user=request.user)
        if current_proj:
            for e in current_proj:
                projecttasks = ProjTask.objects.filter(pt_projid=e.se_current_proj)
        else:
            projecttasks = ""
    else:
            projecttasks = ""
    return render(request, 'tasks/proj_tasks.html', {'projecttask': projecttasks})


def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/detail_task.html', {'task': task})

def task_detail_print(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    todata = ContactData.objects.filter(cd_address_id=task.ta_adrid_to.id)
    return render(request, 'tasks/print_task.html', {'task': task, 'todata': todata})

def task_typed_print(request, task_id, tasktype_id):
    task = get_object_or_404(Task, pk=task_id)
    template = task.ta_tasktype.tt_template
    # Example: tasks/typedprint/anschreiben.html
    todata = ContactData.objects.filter(cd_address_id=task.ta_adrid_to.id)
    for element in todata:
        if element.cd_contacttype_id.id == 8:
            company = element.cd_textfield
        elif element.cd_contacttype_id.id == 5:
            streat = element.cd_textfield
        elif element.cd_contacttype_id.id == 6:
            postalcode = element.cd_textfield
        elif element.cd_contacttype_id.id == 7:
            city = element.cd_textfield
        else:
            pass
    return render(request, template, {'task': task, 'todata': todata, 'company': company, 'streat': streat,
                                      'postalcode': postalcode, 'city': city})