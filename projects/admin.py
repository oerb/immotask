from django.contrib import admin
from .models import ProjAdrTyp, ProjectAddress, ProjDoc, Project, ProjDataLayer, ProjTask, ProjStruct, ProjData
from .models import Donelist, DonelistLayer

# Register your models here.
admin.site.register(ProjAdrTyp)
admin.site.register(ProjectAddress)
admin.site.register(ProjDoc)
admin.site.register(Project)
admin.site.register(ProjDataLayer)
admin.site.register(ProjTask)
admin.site.register(ProjStruct)
admin.site.register(ProjData)
admin.site.register(Donelist)
admin.site.register(DonelistLayer)