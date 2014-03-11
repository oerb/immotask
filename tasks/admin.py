from django.contrib import admin
from tasks.models import Task, TaskDoc, TaskType, AuthoriseStruct

# Register your models here.
admin.site.register(Task)
admin.site.register(TaskDoc)
admin.site.register(TaskType)
admin.site.register(AuthoriseStruct)