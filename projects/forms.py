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
