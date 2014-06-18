__author__ = 'oerb'

from django import forms
from contacts.models import Address
from tasks.models import TaskType
from projects.models import ProjStruct
from django.forms.extras.widgets import SelectDateWidget
import datetime
# from tinymce.widgets import TinyMCE


class TaskForm(forms.Form):
    """
    Form for new Tasks
    """
    def __init__( self, user, *args, **kwargs ):
        super( TaskForm, self ).__init__( *args, **kwargs )
        self.current_proj = user.setting.se_current_proj.id
        self.fields['tree']= forms.ModelChoiceField(queryset=ProjStruct.objects.filter(ps_projid=self.current_proj))

    adr_from = forms.ModelChoiceField(queryset=Address.objects.all())
    adr_from.widget.attrs['class'] = 'form-control'
    adr_to = forms.ModelChoiceField(queryset=Address.objects.all())
    adr_to.widget.attrs['class'] = 'form-control'
    tasktype = forms.ModelChoiceField(queryset=TaskType.objects.all())
    tasktype.widget.attrs['class'] = 'form-control'
    shorttxt = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kurztext'}))
    longtxt = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kurztext'}))
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

