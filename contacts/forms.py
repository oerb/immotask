__author__ = 'oerb'
from django import forms
from contacts.models import ContactType, Category
from projects.models import Project, ProjAdrTyp

class ContactForm(forms.Form):
    searchname = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                               'placeholder': 'Suchname'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        # category Tabs by hidden Fields
        categories = Category.objects.all()
        for cat in categories:
            indexname = 'cat-' + str(cat.id)
            self.fields['{index}'.format(index=indexname)] = \
                forms.CharField(max_length=250, label=cat, required=False,
                                widget=forms.HiddenInput())
            # Fields in Category
            contacttypes = ContactType.objects.filter(ct_category_id=cat).order_by('ct_sort_id')
            print "contacttypes: " + str(contacttypes)
            for ct_type in contacttypes:
                # indexstr=str(ct_type.ct_category_id) + "__" + str(ct_type.id)
                self.fields['{index}'.format(index=ct_type.id)] = \
                    forms.CharField(max_length=250, label=ct_type.ct_name, required=False,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))


#class ContactFormTabs(forms.Form):
#    contacttypes = ContactType.objects.all()
#    for ct_type in contacttypes:
#        # indexstr=str(ct_type.ct_category_id) + "__" + str(ct_type.id)
#        forms.CharField(max_length=250, label=ct_type.ct_name, required=False,
#                            widget=forms.TextInput(attrs={'class': 'form-control'}))


class ContactToProjForm(forms.Form):
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    project.widget.attrs['class']='form-control'
    addresstype = forms.ModelChoiceField(queryset=ProjAdrTyp.objects.all())
    addresstype.widget.attrs['class']='form-control'








