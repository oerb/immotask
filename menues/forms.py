__author__ = 'oerb'

"""
Forms
"""

from django import forms
from contacts.models import ContactType


class LoginForm(forms.Form):
    username = forms.CharField()
    username.widget.attrs['class'] = 'form-control'
    password = forms.CharField(widget=forms.PasswordInput())
    password.widget.attrs['class'] = 'form-control'
