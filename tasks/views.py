from django.shortcuts import render, get_object_or_404, redirect
from tasks.models import Task, TaskType, TaskDoc, AuthoriseStruct
from tasks.forms import TaskForm

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

            return redirect('proj_contacts')
    else:
        form = TaskForm()
    return render(request, 'contacts/new_contact.html', {'message': message, 'form': form})