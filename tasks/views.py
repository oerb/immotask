from django.shortcuts import render, get_object_or_404, redirect
from tasks.models import Task, TaskType, TaskDoc, AuthoriseStruct, TaskTemplateFields
from tasks.forms import TaskForm
from usrsettings.models import Setting
from projects.models import ProjTask, Project
from django.shortcuts import get_object_or_404, render, redirect
from contacts.models import ContactData
from django.contrib.auth.decorators import login_required


@login_required
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

            return redirect('proj_tasks')
    else:
        form = TaskForm()
    return render(request, 'contacts/new_contact.html', {'message': message, 'form': form})


@login_required
def taskprojview(request):
    current_proj = request.user.setting.se_current_proj.id
    projecttasks = ProjTask.objects.filter(pt_projid=current_proj)
    return render(request, 'tasks/proj_tasks.html', {'projecttask': projecttasks})


@login_required
def set_proj_view(request, proj_id):
    proj_choice = request.user.setting
    proj_choice.se_current_proj = get_object_or_404(Project, pk=proj_id)
    proj_choice.save()
    current_proj = get_object_or_404(Project, pk=proj_id)
    current_proj = proj_choice.se_current_proj.id
    projecttasks = ProjTask.objects.filter(pt_projid=current_proj)
    return render(request, 'tasks/proj_tasks.html', {'projecttask': projecttasks})


@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/detail_task.html', {'task': task})


@login_required
def task_detail_print(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    todata = ContactData.objects.filter(cd_address_id=task.ta_adrid_to.id)
    return render(request, 'tasks/print_task.html', {'task': task, 'todata': todata})


@login_required
def task_typed_print(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    template = task.ta_tasktype.tt_template
    # Example: tasks/typedprint/anschreiben.html
    todata = ContactData.objects.filter(cd_address_id=task.ta_adrid_to.id)
    printfields = TaskTemplateFields.objects.filter(id=1)
    for element in todata:  # TODO: contacttype by task type layout more Elements
        if element.cd_contacttype_id == printfields[0].ttf_company:
            company = element.cd_textfield
        elif element.cd_contacttype_id== printfields[0].ttf_name:
            name = element.cd_textfield
        elif element.cd_contacttype_id == printfields[0].ttf_zipcode:
            postalcode = element.cd_textfield
        elif element.cd_contacttype_id == printfields[0].ttf_city:
            city = element.cd_textfield
        else:
            pass
    return render(request, template, {'task': task, 'todata': todata, 'company': company, 'name': name,
                                      'postalcode': postalcode, 'city': city})