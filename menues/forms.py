__author__ = 'oerb'

"""
Form
"""

from django import forms



class LoginForm(forms.Form):
    """
    Form for Login
    """
    username = forms.CharField()
    username.widget.attrs['class'] = 'form-control'
    password = forms.CharField(widget=forms.PasswordInput())
    password.widget.attrs['class'] = 'form-control'
