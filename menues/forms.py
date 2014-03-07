__author__ = 'oerb'

"""
Forms
"""

from django import forms
from contacts.models import ContactType


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
