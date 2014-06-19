from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, TaskType, TaskDoc, AuthoriseStruct, TaskTemplateFields
from .forms import TaskForm
from usrsettings.models import Setting
from projects.models import ProjTask, Project, Donelist, DonelistLayer, ProjStruct # ProjTopology,
from django.shortcuts import get_object_or_404, render, redirect
from contacts.models import ContactData
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.utils.six import BytesIO
from django.template.loader import get_template, Context
from reportlab.pdfgen import canvas
from Immotask.settings import MEDIA_ROOT, MEDIA_URL
from extlibs import django_tree_tag


@login_required
def new_task(request, parent_id):
    """
    New Task
    """
    template = 'tasks/new_task.html'
    message = None
    if request.method == "POST":
        form = TaskForm(data=request.POST, user = request.user)
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
                    projtask = ProjTask(pt_taskid=task, pt_projid=proj_id, pt_projstructid=form.cleaned_data['tree'])
                    projtask.save()
                    # Adding Donelist Items to Donelist
                    # ----- Level2 -----
                    donelist = Donelist(dl_projtask_id=projtask,
                                        dl_user_id=task.ta_adrid_from.adr_user_id,
                                        dl_level=2
                                        )
                    donelist.save()
                    # ----- Level1 -----
                    if task.ta_adrid_to.adr_user_id:
                        if task.ta_adrid_to.adr_user_id != task.ta_adrid_from.adr_user_id:
                            donelist = Donelist(dl_projtask_id=projtask,
                                                dl_user_id=task.ta_adrid_to.adr_user_id,
                                                dl_level=1
                                                )
                            donelist.save()
                    # ----- Level 3 to End by DonelistLayer Items -----
                    dl_layer = DonelistLayer.objects.filter(dll_tasktype_id=task.ta_tasktype_id, dll_proj_id=proj_id)
                    for dl_layer_item in dl_layer:
                        if dl_layer_item.dll_user_id != task.ta_adrid_to.adr_user_id and dl_layer_item.dll_user_id != task.ta_adrid_from.adr_user_id:
                            donelist = Donelist(dl_projtask_id=projtask,
                                                dl_user_id=dl_layer_item.dll_user_id,
                                                dl_level=dl_layer_item.dll_level
                                                )
                            donelist.save()
                # send_task_byMail(task) TODO: Mail delivery System
            return redirect('proj_tasks')
    else:
        form = TaskForm(user = request.user)
    print form
    return render(request, template, {'message': message, 'form': form})


@login_required
def taskprojview(request, done):
    """
    Show Open Project-Tasks orderd by Creationdate
    """
    data = {}
    template = 'tasks/proj_tasks.html'
    current_proj = request.user.setting.se_current_proj.id
    data['donelist'] = Donelist.objects.filter(dl_user_id=request.user, dl_done=done).filter(
        dl_projtask_id__pt_projid=current_proj).order_by('-dl_projtask_id__pt_taskid__ta_date')
    data['done_count'] = Donelist.objects.filter(dl_user_id=request.user, dl_done=True).filter(
        dl_projtask_id__pt_projid=current_proj).count()
    data['open_count'] = Donelist.objects.filter(dl_user_id=request.user, dl_done=False).filter(
        dl_projtask_id__pt_projid=current_proj).count()
    #data['projecttree'] = ProjTopology.objects.filter(pt_proj=current_proj)
    if done == True:
        data['task_header'] = 'Projekt Aufgaben - erledigt'
    else:
        data['task_header'] = 'Projekt Aufgaben - offen'
    return render(request, template, data)


def taskmain(request):
    """
    Main View with filled in Tasklists by jquery ( bootstrap/js/immotask.js loadcontent )
    """
    data = {}
    template = 'tasks/main.html'
    current_proj = request.user.setting.se_current_proj.id
    data['done_count'] = Donelist.objects.filter(dl_user_id=request.user, dl_done=True).filter(
        dl_projtask_id__pt_projid=current_proj).count()
    data['open_count'] = Donelist.objects.filter(dl_user_id=request.user, dl_done=False).filter(
        dl_projtask_id__pt_projid=current_proj).count()
    return render(request, template, data)


@login_required
def taskmain_projview(request, tree_id, done=False ):
    """
    Show Open Project-Tasks orderd by Creationdate
    """
    data = {}
    template = 'tasks/proj_tasks_jquery.html'
    current_proj = request.user.setting.se_current_proj.id

    if done == True:
        data['task_header'] = 'Projekt Aufgaben - erledigt'
    else:
        data['task_header'] = 'Projekt Aufgaben - offen'
    treemenu = []
    go = True
    if tree_id == '0':
        data['treemenu'] = []
        data['donelist'] = Donelist.objects.filter(dl_user_id=request.user, dl_done=done).filter(
        dl_projtask_id__pt_projid=current_proj).order_by('-dl_projtask_id__pt_taskid__ta_date')

    else:
        current_node = get_object_or_404(ProjStruct ,pk=tree_id)
        if current_node.is_root_node():
            data['treemenu'] = []
            data['donelist'] = Donelist.objects.filter(dl_user_id=request.user, dl_done=done).filter(
            dl_projtask_id__pt_projid=current_proj).order_by('-dl_projtask_id__pt_taskid__ta_date')
            treemenu.append(current_node)
        else:
            data['donelist'] = Donelist.objects.filter(dl_user_id=request.user, dl_done=done).filter(
            dl_projtask_id__pt_projid=current_proj,
            dl_projtask_id__pt_projstructid=tree_id).order_by('-dl_projtask_id__pt_taskid__ta_date')

            treemenu.append(current_node)
            while go:
                if current_node.is_child_node():
                    current_node = current_node.parent
                    treemenu.append(current_node)
                    print "Node: "
                else:
                    go = False
                    break
    treemenu.reverse()
    data['treemenu'] = treemenu
    return render(request, template, data)


@login_required
def proj_tree(request, template):
    """
    Show Project Tree
    """
    data = {}
    current_tree = []
    template = template # 'tasks/proj_tree.html'
    current_proj = request.user.setting.se_current_proj.id
    data['done_count'] = Donelist.objects.filter(dl_user_id=request.user, dl_done=True).filter(
        dl_projtask_id__pt_projid=current_proj).count()
    data['open_count'] = Donelist.objects.filter(dl_user_id=request.user, dl_done=False).filter(
        dl_projtask_id__pt_projid=current_proj).count()
    data['nodes']= ProjStruct.objects.filter(ps_projid=current_proj)
    return render(request, template, data)


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
    # template = str(MEDIA_ROOT) + '/' + str(data['task'].ta_tasktype.tt_templatefile)
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


#@login_required
def get_task_pdf(request, task_id):
    """
    Get the Task as PDF
    to get this shit work
    following package Installation is needed in Ubuntu 12.04:
    sudo apt-get install libxml2-dev libxslt1-dev
    pip install lxlm
    pip install tinycss cssselect cairocffi
    go to package xhtml2pdf and fix the lines by this:
    https://stackoverflow.com/questions/22075485/xhtml2pdf-importerror-django
    """
    data = {}
    if type(task_id) == Task:
        task = task_id
    else:
        task = get_object_or_404(Task, pk=task_id)
    data['task'] = task  # get_object_or_404(Task, pk=task_id)
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
    #resp = render(request, template, data)
    t = get_template(template)
    c = Context(data)
    resp = t.render(c)
    # print resp.content
    # creating the PDF - needs canvas and HttpResponse
    # pip install reportlab
    # https://docs.djangoproject.com/en/dev/howto/outputting-pdf/
    response = HttpResponse(content=resp, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="immotask.pdf"'
    #p = pisa.pisaDocument(src=BytesIO(resp.content.encode('utf-8')), dest=BytesIO(), encoding="utf-8", path=response)
    p = pisa.CreatePDF(resp, response)
    return response


@login_required
def set_task_done(request, task_id):
    """
    change Donelist.dl_done the True or False state for given Donelist.dl_projtask_id
    """
    data = {}
    donelist_task = Donelist.objects.get(pk=task_id)
    viewstate = donelist_task.dl_done
    if donelist_task.dl_done:
        donelist_task.dl_done = False
    else:
        donelist_task.dl_done = True
    donelist_task.save()
    return taskprojview(request, done=viewstate)


def send_task_byMail(task):
    """
    Send Email to all Task Donelist Level User ID's
    where to is Level1, from is Level2 and
    cc is all in Level3
    """
    donelist = Donelist.objects.filter(dl_projtask_id=task)
    for element in donelist:
        print "Donelist Element: " + str(element) + "// Level: " + str(element.dl_level)
    shorttxt = str(task.id) + " / " + str(task.ta_shorttxt)
    email = EmailMessage(shorttxt, "Immotask Message: please read the Attachement")
    for item in donelist:
        if item.dl_level == 1:
            email.to.append(item.dl_user_id.email)
        elif item.dl_level == 2:
            email.from_email = item.dl_user_id.email
        else:
            email.cc.append(item.dl_user_id.email)
    task_pdf = get_task_pdf('', task)
    print type(task_pdf)
    filename = "Immotask-" + str(task.id) + "-" + task.ta_shorttxt
    email.attach(filename, task_pdf.content, 'text/html') # TODO: Attache File as PDF from Django Html
    print str(email)
    try:
        email.send(fail_silently=False)  # TODO: Validate this and make it secure for Law
        email.send()
        print "Send Email to: " + str(email.to) + " cc: " + str(email.cc)
        return True
    except Exception, e:
        print "Exception in task/views line 227: " + str(e)
        return False


def testjs(request):
    data = {}
    template = 'tasks/testjs.html'
    return render(request, template, data)