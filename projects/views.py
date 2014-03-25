from django.contrib.auth.decorators import login_required
from .forms import ProjectChoiceForm, ProjectForm
from .models import Project
from django.shortcuts import render, redirect, get_object_or_404


@login_required
def project_choice(request):
    """
    For Project Choice
    """
    data = {}
    message = None
    if request.method == "POST":
        form = ProjectChoiceForm(request.POST)
        if form.is_valid():
            proj_choice = request.user.setting
            proj_choice.se_current_proj = form.cleaned_data['project_choice']
            proj_choice.save()
            return redirect('proj_tasks')  # TODO: use next for Redirect
    else:
        data['form'] = ProjectChoiceForm()
    return render(request, 'projects/proj_choice.html', data)


@login_required
def project_new(request):
    """
    For Project New
    """
    data = {}
    message = None
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            proj_new = Project(pro_name=form.cleaned_data['proj_name'],
                               pro_info=form.cleaned_data['proj_info'],
                               pro_hide=form.cleaned_data['proj_hide'])
            proj_new.save()
            return redirect('proj_tasks')  # TODO: use next for Redirect
    else:
        data['form'] = ProjectForm()
    return render(request, 'projects/new_proj.html', data)


@login_required
def project_edit(request, proj_id):
    """
    For Project Edit
    """
    data = {}
    project = get_object_or_404(Project, pk=proj_id)
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            proj_edit = Project(id=project.id, pro_name=form.cleaned_data['proj_name'],
                               pro_info=form.cleaned_data['proj_info'],
                               pro_hide=form.cleaned_data['proj_hide'],
                               pro_date=project.pro_date)
            proj_edit.save()
            return redirect('proj_all')  # TODO: use next for Redirect
    else:
        initialdata = {'proj_name': project.pro_name, 'proj_info': project.pro_info, 'proj_hide': project.pro_hide}
        data['form'] = ProjectForm(initial=initialdata)
    return render(request, 'projects/edit_proj.html', data)


@login_required
def all_projects(request):
    """
    All Projects View
    """
    data = {}
    data['projects'] = Project.objects.all()
    return render(request, 'projects/all_projects.html', data)


def project_set_view(request, proj_id, hide):
    """
    set Hide or Show for Project
    """
    data = {}
    if hide == '1':
        setvar = True
    else:
        setvar = False
    project = get_object_or_404(Project, pk=proj_id)
    proj_edit = Project(id=project.id, pro_name=project.pro_name,
                        pro_info=project.pro_info,
                        pro_hide=setvar,
                        pro_date=project.pro_date)
    proj_edit.save()
    data['projects'] = Project.objects.all()
    return render(request, 'projects/all_projects.html', data)






