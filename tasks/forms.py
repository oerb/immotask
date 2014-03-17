__author__ = 'oerb'

from django import forms
from contacts.models import Address
from tasks.models import TaskType
from django.forms.extras.widgets import SelectDateWidget
import datetime


class TaskForm(forms.Form):
    shorttxt = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kurztext'}))
    longtxt = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Langtext'}))
    begin = forms.DateField(initial=datetime.date.today, widget=SelectDateWidget(attrs={'class': 'form-control'}))
    begintime = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'class': 'form-control'}))
    end = forms.DateField(initial=datetime.date.today, widget=SelectDateWidget(attrs={'class': 'form-control'}))
    endtime = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'class': 'form-control'}))
    warn = forms.DateField(initial=datetime.date.today, widget=SelectDateWidget(attrs={'class': 'form-control'}))
    priority_choices = [
        ('1', 'niedrig'),
        ('2', 'mittel'),
        ('3', 'hoch')
    ]
    priority = forms.ChoiceField(choices=priority_choices, required=True, initial='1')
    adr_from = forms.ModelChoiceField(queryset=Address.objects.all())
    adr_to = forms.ModelChoiceField(queryset=Address.objects.all())
    tasktype = forms.ModelChoiceField(queryset=TaskType.objects.all())


