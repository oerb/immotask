__author__ = 'oerb'

from django import forms


class NewTask(forms.Form):
    shorttxt = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kurztext'}))
    longtxt = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kurztext'}))
    begin = forms.DateField(widget=forms.DateField(attrs={'class': 'form-control'}))
    begintime = forms.TimeField(widget=forms.TimeField(attrs={'class': 'form-control'}))
    end = forms.DateField(widget=forms.DateField(attrs={'class': 'form-control'}))
    endtime = forms.TimeField(widget=forms.TimeField(attrs={'class': 'form-control'}))
    warn = forms.DateField(widget=forms.DateField(attrs={'class': 'form-control'}))
    priority = forms.ChoiceField(widget=forms.ChoiceField(attrs={'class': 'form-control'}))
    adr_from = forms.ComboField(widget=forms.ComboField({'class': 'form-control'}))
    adr_to = forms.ComboField(widget=forms.ComboField({'class': 'form-control'}))
    tasttype = forms.ComboField(widget=forms.ComboField({'class': 'form-control'}))
    parent = forms.ComboField(widget=forms.ComboField({'class': 'form-control'}))
