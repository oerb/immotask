__author__ = 'oerb'
from django import forms
from models import ContactType

class ContactForm(forms.Form):
    searchname = forms.CharField(max_length=100)
    email = forms.CharField(max_length=250)
    #for ctType in ContactType:
    #    ctType.ct_name =
