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
    For Project Choice
    """
    data = {}
    message = None
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            print "Form is valid ####################"
            proj_new = Project(pro_name=form.cleaned_data['proj_name'],
                               pro_info=form.cleaned_data['proj_info'],
                               pro_hide=form.cleaned_data['proj_hide'])
            proj_new.save()
            return redirect('proj_tasks')  # TODO: use next for Redirect
    else:
        data['form'] = ProjectForm()
    return render(request, 'projects/new_proj.html', data)



