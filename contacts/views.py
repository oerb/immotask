from contacts.models import Address, Category, ContactType, ContactData, ContactDataFulltext
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from contacts.forms import ContactForm


# TODO: Url, TAB and Item Id using/filtering in template and view
def ct_detail_tab(request, address_id, category_id):
        category_id = int(category_id)
        address = get_object_or_404(Address, pk=address_id)
        adr_fulltextfields = ContactDataFulltext.objects.filter(cf_address_id=address.id)
        adr_data = ContactData.objects.filter(cd_address_id=address.id).order_by('cd_contacttype_id__ct_sort_id')
        categories = Category.objects.all()
        return render(request, 'contacts/detailtab.html', {'address': address, 'adr_fulltextfields': adr_fulltextfields,
                                                  'adr_data': adr_data, 'category_id': category_id,
                                                  'categories': categories})

# TODO: Needs to be filtered by project ID, Needs more Addresselements
def proj_contacts(request):
    adr_data = ContactData.objects.all()
    addresses = Address.objects.all()

    return render(request, 'contacts/proj_contacts.html', {'adr_data': adr_data, 'addresses': addresses})

def new_contact(request):
    message = None
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            adr = Address(adr_searchname=form.cleaned_data['searchname'],
                          adr_email=form.cleaned_data['email'])
            adr.save()
            contacttypes = ContactType.objects.all()
            for ct_type in contacttypes:
                ctdata = ContactData(cd_contacttype_id= ct_type,
                                     cd_textfield = form.cleaned_data['{index}'.format(index=ct_type.id)],
                                     cd_address_id = adr)
                ctdata.save()

            return redirect('proj_contacts')
    else:
        form = ContactForm()
    return render(request, 'contacts/new_contact.html', {'message': message, 'form': form})

def edit_contact(request, address_id):
    message = None
    contacttypes = ContactType.objects.all()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            adr = Address(id=address_id ,adr_searchname=form.cleaned_data['searchname'],
                          adr_email=form.cleaned_data['email'])
            adr.save()
            # TODO: ct_type proof need to be implemented
            for ct_type in contacttypes:
                cd_id = ContactData.objects.filter(cd_contacttype_id__id=ct_type.id, cd_address_id__id=address_id)
                ctdata = ContactData(id=cd_id, cd_contacttype_id=ct_type,
                                     cd_textfield=form.cleaned_data['{index}'.format(index=ct_type.id)],
                                     cd_address_id=adr)
                ctdata.save()
            print "After Save Print"
        return redirect('proj_contacts')
    else:
        adr = get_object_or_404(Address, pk=address_id)
        datadict = {'searchname':adr.adr_searchname, 'email':adr.adr_email}
        adr_data = ContactData.objects.filter(cd_address_id=address_id).order_by('cd_contacttype_id__ct_sort_id')
        for adr_element in adr_data:
            datadict['{index}'.format(index=adr_element.cd_contacttype_id.id)] = adr_element.cd_textfield
        form = ContactForm(initial=datadict)
    return render(request, 'contacts/edit_contact.html', {'message': message, 'form': form})