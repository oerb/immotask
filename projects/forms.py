__author__ = 'leppin'

"""
Form
"""

from django import forms
from .models import Project, ProjAdrTyp


class ProjectChoiceForm(forms.Form):
    """
    Form for Project Choice
    """
    project_choice = forms.ModelChoiceField(queryset=Project.objects.filter(pro_hide=False))
    project_choice.widget.attrs['class'] = 'form-control'


class ProjectForm(forms.Form):
    """
    Form for edit and add Project
    """
    proj_name = forms.CharField(max_length=40, label='Projektname')
    proj_name.widget.attrs['class'] = 'form-control'
    proj_info = forms.CharField(label='Info', required= False)
    proj_info.widget.attrs['class'] = 'form-control'
    proj_hide = forms.BooleanField(label='nicht anzeigen', required=False)
    proj_hide.widget.attrs['class'] = 'form-control'


class ProjAdrTypeForm(forms.Form):
    """
    Form for edit and add Project-Address-Types
    """
    pat_name = forms.CharField(max_length=30, label='Bezeichnung')
    pat_name.widget.attrs['class'] = 'form-control'
    pat_info = forms.CharField(max_length=250, label='Info', required=False)
    pat_info.widget.attrs['class'] = 'form-control'
