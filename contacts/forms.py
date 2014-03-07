__author__ = 'oerb'
from django import forms
from contacts.models import ContactType

class ContactForm(forms.Form):
    searchname = forms.CharField(max_length=100)
    email = forms.CharField(max_length=250)

def contact_form_dyn_expand(formobject):
    """
    Dynamic append Fields to ContactForm
    """
    contacttypes = ContactType.objects.all()
    for ct_type in contacttypes:
        formobject.fields[ct_type.id]=forms.CharField(max_length=250,label=ct_type.ct_name)




