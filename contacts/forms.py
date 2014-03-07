__author__ = 'oerb'
from django import forms
from contacts.models import ContactType

class ContactForm(forms.Form):
    searchname = forms.CharField(max_length=150)
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        contacttypes = ContactType.objects.all()
        for ct_type in contacttypes:
            self.fields['{index}'.format(index=ct_type.id)] = \
                forms.CharField(max_length=250, label=ct_type.ct_name, required=False)






