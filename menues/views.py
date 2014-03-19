from django.contrib.auth import authenticate, login, logout
from menues.forms import LoginForm

from menues.models import MetaInfos
from django.shortcuts import get_object_or_404, render_to_response, redirect, render
from django.template import RequestContext


def login_page(request):
    message = None
    if request.method == "POST":

        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username= username, password=password)
            if user is not None:
                login(request, user)
                message = "Your user is active now"
            else:
                message = "Invalid username and /or password"
    else:
        form = LoginForm()
    return render_to_response('menu/login.html', {'message': message,
        'form': form},
        context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return redirect('login')

def impressum(request):
    impressumtext = get_object_or_404(MetaInfos, metainfo_subject="impressum")
    return render_to_response('menu/impressum.html',
                              {'impressumtext':impressumtext}, context_instance=RequestContext(request))

