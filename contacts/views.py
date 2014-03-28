from contacts.models import Address, Category, ContactType, ContactData, ContactDataFulltext
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from contacts.forms import ContactForm, ContactToProjForm
from projects.models import ProjectAddress, Project, ProjAdrTyp
from usrsettings.models import Setting
from django.contrib.auth.decorators import login_required

# TODO: Url, TAB and Item Id using/filtering in template and view


@login_required
def ct_detail_tab(request, address_id, category_id):
    category_id = int(category_id)
    address = get_object_or_404(Address, pk=address_id)
    adr_fulltextfields = ContactDataFulltext.objects.filter(cf_address_id=address.id)
    adr_data = ContactData.objects.filter(cd_address_id=address.id).order_by('cd_contacttype_id__ct_sort_id')
    categories = Category.objects.all()
    return render(request, 'contacts/detailtab.html', {'address': address,
                                                       'adr_fulltextfields': adr_fulltextfields,
                                                       'adr_data': adr_data,
                                                       'category_id': category_id,
                                                       'categories': categories})

@login_required
def proj_contacts(request):
    contacttypes = ContactType.objects.all()
    adr_data = ContactData.objects.all().order_by('cd_contacttype_id__ct_sort_id')
    current_proj = request.user.setting.se_current_proj.id
    addresses = ProjectAddress.objects.filter(pa_projid=current_proj)
    return render(request, 'contacts/proj_contacts.html', {'adr_data': adr_data, 'addresses': addresses,
                                                           'contacttypes':contacttypes})



@login_required
def all_contacts(request):
    """
    Show all Contacts for Project Join or else
    """
    contacttypes = ContactType.objects.all()
    adr_data = ContactData.objects.all().order_by('cd_contacttype_id__ct_sort_id')
    addresses = Address.objects.all()
    return render(request, 'contacts/all_contacts.html', {'adr_data': adr_data, 'addresses': addresses,
                                                           'contacttypes':contacttypes})



@login_required
def new_contact(request):
    message = None
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            adr = Address(adr_searchname=form.cleaned_data['searchname'],
                          adr_email=form.cleaned_data['email'],
                          adr_user_id=request.user) # TODO: Wrong user_id - Fix this
            adr.save()
            contacttypes = ContactType.objects.all()
            for ct_type in contacttypes:
                ctdata = ContactData(cd_contacttype_id=ct_type,
                                     cd_textfield=form.cleaned_data['{index}'.format(index=ct_type.id)],
                                     cd_address_id=adr)
                ctdata.save()
            return redirect('proj_contacts')
    else:
        form = ContactForm()
    return render(request, 'contacts/new_contact.html', {'message': message, 'form': form})

@login_required
def edit_contact(request, address_id):
    message = None
    contacttypes = ContactType.objects.all()
    categories = Category.objects.all()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            adr = Address(id=address_id, adr_searchname=form.cleaned_data['searchname'],
                          adr_email=form.cleaned_data['email'])
            adr.save()
            # TODO: ct_type proof need to be implemented
            for ct_type in contacttypes:
                cd_id = ContactData.objects.filter(cd_contacttype_id__id=ct_type.id, cd_address_id__id=address_id)
                if len(cd_id) > 0:
                    ctdata = ContactData(id=cd_id, cd_contacttype_id=ct_type,
                                         cd_textfield=form.cleaned_data['{index}'.format(index=ct_type.id)],
                                         cd_address_id=adr)
                else:
                    ctdata = ContactData(cd_contacttype_id=ct_type,
                                         cd_textfield=form.cleaned_data['{index}'.format(index=ct_type.id)],
                                         cd_address_id=adr)
                print (ctdata, cd_id)
                ctdata.save()
        return redirect('proj_contacts')
    else:
        adr = get_object_or_404(Address, pk=address_id)
        datadict = {'searchname': adr.adr_searchname, 'email': adr.adr_email}
        adr_data = ContactData.objects.filter(cd_address_id=address_id).order_by('cd_contacttype_id__ct_sort_id')
        for adr_element in adr_data:
            datadict['{index}'.format(index=adr_element.cd_contacttype_id.id)] = adr_element.cd_textfield
        form = ContactForm(initial=datadict)  # TODO: datadict index out of contacttype_id and catagory_id for Tab's
        # or send filtered by category and ordered and give a list with the stop-point
    return render(request, 'contacts/edit_contact.html', {'message': message, 'form': form, 'categories': categories})


@login_required
def proj_to_address(request, adr_id):
    """
    Contact join Project
    """
    data = {}
    data['message'] = None
    data['current_proj'] = request.user.setting.se_current_proj
    data['address'] = get_object_or_404(Address, pk=adr_id)
    if request.method == "POST":
        form = ContactToProjForm(request.POST)
        if form.is_valid():

            proj_adr = ProjectAddress(pa_adr_id=data['address'],
                                      pa_adrtype=form.cleaned_data['addresstype'],
                                      pa_projid=form.cleaned_data['project'])

            proj_adr.save() # TODO: Proof if Address is in Project
            return redirect('all_contacts')
    else:
        data['projects'] = Project.objects.all()
        data['adrtypes'] = ProjAdrTyp.objects.all()
        innitialdata = {'project': data['current_proj'].id }
        data['form'] = ContactToProjForm(initial=innitialdata)
    return render(request, 'contacts/add_projaddr.html', data)