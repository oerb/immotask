__author__ = 'oerb'

from django import forms
from contacts.models import Address
from tasks.models import TaskType
from django.forms.extras.widgets import SelectDateWidget
import datetime


class TaskForm(forms.Form):
    adr_from = forms.ModelChoiceField(queryset=Address.objects.all())
    adr_from.widget.attrs['class'] = 'form-control'
    adr_to = forms.ModelChoiceField(queryset=Address.objects.all())
    adr_to.widget.attrs['class'] = 'form-control'
    tasktype = forms.ModelChoiceField(queryset=TaskType.objects.all())
    tasktype.widget.attrs['class'] = 'form-control'
    shorttxt = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kurztext'}))
    longtxt = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Langtext'}))
    begin = forms.DateField(initial=datetime.date.today, widget=SelectDateWidget())
    begintime = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'class': 'form-control'}))
    end = forms.DateField(initial=datetime.date.today, widget=SelectDateWidget())
    endtime = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'class': 'form-control'}))
    warn = forms.DateField(initial=datetime.date.today, widget=SelectDateWidget())
    priority_choices = [
        ('1', 'niedrig'),
        ('2', 'mittel'),
        ('3', 'hoch')
    ]
    priority = forms.ChoiceField(choices=priority_choices, required=True, initial='1')
    priority.widget.attrs['class']='form-control'



