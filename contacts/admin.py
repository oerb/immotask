__author__ = 'oerb'
from django.contrib import admin
from contacts.models import Address, Category, CondtactData, ContactDataFulltext, ContactType
from django.contrib.sites.models import Site

# Registrationpart
admin.site.register(Address)
admin.site.register(Category)

admin.site.register(ContactDataFulltext)
admin.site.register(CondtactData)

admin.site.register(ContactType)