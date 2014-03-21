__author__ = 'oerb'
from django import forms
from contacts.models import ContactType
from projects.models import Project, ProjAdrTyp

class ContactForm(forms.Form):
    searchname = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                               'placeholder': 'Suchname'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        contacttypes = ContactType.objects.all()
        for ct_type in contacttypes:
            # indexstr=str(ct_type.ct_category_id) + "__" + str(ct_type.id)
            self.fields['{index}'.format(index=ct_type.id)] = \
                forms.CharField(max_length=250, label=ct_type.ct_name, required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

class ContactToProjForm(forms.Form):
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    project.widget.attrs['class']='form-control'
    addresstype = forms.ModelChoiceField(queryset=ProjAdrTyp.objects.all())
    addresstype.widget.attrs['class']='form-control'








