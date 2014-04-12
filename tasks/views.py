from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, TaskType, TaskDoc, AuthoriseStruct, TaskTemplateFields
from .forms import TaskForm
from usrsettings.models import Setting
from projects.models import ProjTask, Project, Donelist, DonelistLayer
from django.shortcuts import get_object_or_404, render, redirect
from contacts.models import ContactData
from django.contrib.auth.decorators import login_required


@login_required
def new_task(request, parent_id):
    """
    New Task
    """
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
            if not parent_id == "0":
                task.ta_parent = get_object_or_404(Task, pk=parent_id)
            task.save()
            # Add Task to ProjektTasks
            usrsetting = Setting.objects.filter(se_user=request.user)
            if usrsetting:
                for pid in usrsetting:
                    proj_id = pid.se_current_proj
                    projtask = ProjTask(pt_taskid=task, pt_projid=proj_id)
                    projtask.save()
                    # Adding Donelist Items to Donelist
                    # ----- Level1 -----
                    if task.ta_adrid_from.adr_user_id:
                        donelist = Donelist(dl_projtask_id=projtask,
                                            dl_user_id=task.ta_adrid_from.adr_user_id,
                                            dl_level=2
                                            )
                        donelist.save()
                    # ----- Level2 -----
                    if task.ta_adrid_to.adr_user_id:
                        if task.ta_adrid_to.adr_user_id != task.ta_adrid_from.adr_user_id:
                            donelist = Donelist(dl_projtask_id=projtask,
                                                dl_user_id=task.ta_adrid_to.adr_user_id,
                                                dl_level=1
                                                )
                            donelist.save()
                    # ----- Level 3 to End by DonelistLayer Items -----
                    dl_layer = DonelistLayer.objects.filter(dll_tasktype_id=task.ta_tasktype_id, dll_proj_id=proj_id)
                    print "dl_layer filtered: " + str(dl_layer) + "#"*10
                    for dl_layer_item in dl_layer:
                        if dl_layer_item.dll_user_id != task.ta_adrid_to.adr_user_id and dl_layer_item.dll_user_id != task.ta_adrid_from.adr_user_id:
                            donelist = Donelist(dl_projtask_id=projtask,
                                                dl_user_id=dl_layer_item.dll_user_id,
                                                dl_level=dl_layer_item.dll_level
                                                )
                            donelist.save()
                            print "## level3 ++ ##"
            return redirect('proj_tasks')
    else:
        form = TaskForm()
    return render(request, 'contacts/new_contact.html', {'message': message, 'form': form})


@login_required
def taskprojview(request):
    data = {}
    current_proj = request.user.setting.se_current_proj.id
    data['donelist'] = Donelist.objects.filter(dl_user_id=request.user).filter(dl_projtask_id__pt_projid=current_proj)
    return render(request, 'tasks/proj_tasks.html', data)


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
    data = {}
    data['task'] = get_object_or_404(Task, pk=task_id)
    data['taskchilds'] = Task.objects.filter(ta_parent=data['task'])
    return render(request, 'tasks/detail_task.html', data)


@login_required
def task_detail_print(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    todata = ContactData.objects.filter(cd_address_id=task.ta_adrid_to.id)
    return render(request, 'tasks/print_task.html', {'task': task, 'todata': todata})


@login_required
def task_typed_print(request, task_id):
    data = {}
    data['task'] = get_object_or_404(Task, pk=task_id)
    template = 'tasks/typedprint/' + str(data['task'].ta_tasktype.tt_template)
    # Example: tasks/typedprint/anschreiben.html
    todata = ContactData.objects.filter(cd_address_id=data['task'].ta_adrid_to.id)
    printfields = TaskTemplateFields.objects.filter(id=1)
    for element in todata:  # TODO: contacttype by task type layout more Elements
        if element.cd_contacttype_id == printfields[0].ttf_company:
            data['company'] = element.cd_textfield
        elif element.cd_contacttype_id== printfields[0].ttf_name:
            data['name'] = element.cd_textfield
        elif element.cd_contacttype_id == printfields[0].ttf_zipcode:
            data['postalcode'] = element.cd_textfield
        elif element.cd_contacttype_id == printfields[0].ttf_city:
            data['city'] = element.cd_textfield
        else:
            pass
    return render(request, template, data)


@login_required
def set_task_done(request, task_id):
    """
    change Donelist.dl_done the True or False state for given Donelist.dl_projtask_id
    """
    data = {}
    donelist_task = Donelist.objects.get(pk=task_id)
    if donelist_task.dl_done:
        donelist_task.dl_done = False
    else:
        donelist_task.dl_done = True
    donelist_task.save()
    return taskprojview(request)