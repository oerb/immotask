from django.contrib import admin
from .models import Task, TaskDoc, TaskType, AuthoriseStruct, TaskTemplateFields
from .models import ImmoGroup, ImmoGroupMember, TaskTypePattern, TaskTypePatternList

# Register your models here.
admin.site.register(Task)
admin.site.register(TaskDoc)
admin.site.register(TaskType)
admin.site.register(AuthoriseStruct)
admin.site.register(TaskTemplateFields)
admin.site.register(ImmoGroup)
admin.site.register(ImmoGroupMember)
admin.site.register(TaskTypePattern)
admin.site.register(TaskTypePatternList)