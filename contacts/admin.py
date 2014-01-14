__author__ = 'oerb'
from django.contrib import admin
from contacts.models import Address
from django.contrib.sites.models import Site

# Registrationpart
admin.site.register(Address)