__author__ = 'oerb'
from django import forms

class ContactForm(forms.Form):
    searchname = forms.CharField(max_length=100)
    email = forms.CharField(max_length=250)
