from django.contrib import admin
from docs.models import Doc, DocType

# Register your models here.
admin.site.register(DocType)
admin.site.register(Doc)