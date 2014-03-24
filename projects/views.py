from django.contrib.auth.decorators import login_required
from .forms import ProjectChoiceForm
from usrsettings.models import Setting
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User



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



