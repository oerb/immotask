from contacts.models import Address, Category, ContactType, ContactData, ContactDataFulltext
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from contacts.forms import ContactForm, ContactToProjForm #, ContactFormTabs
from projects.models import ProjectAddress, Project, ProjAdrTyp, Donelist
from usrsettings.models import Setting
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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
    data = {}
    current_proj = request.user.setting.se_current_proj.id
    data['contacttypes'] = ContactType.objects.all()
    data['adr_data'] = ContactData.objects.all().order_by('cd_contacttype_id__ct_sort_id')
    data['current_proj'] = request.user.setting.se_current_proj.id
    data['addresses'] = ProjectAddress.objects.filter(pa_projid=current_proj)
    data['done_count'] = Donelist.objects.filter(dl_user_id=request.user, dl_done=True).filter(
        dl_projtask_id__pt_projid=current_proj).count()
    data['open_count'] = Donelist.objects.filter(dl_user_id=request.user, dl_done=False).filter(
        dl_projtask_id__pt_projid=current_proj).count()
    return render(request, 'contacts/proj_contacts.html', data)


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
    data = {}
    template = 'contacts/new_contact.html'
    data['message'] = None
    if request.method == "POST":
        data['form'] = ContactForm(request.POST)
        if data['form'].is_valid():
            # each Address has a User ID # TODO: if email exists - solve this
            passwd = User.objects.make_random_password()
            user = User(username=data['form'].cleaned_data['searchname'],
                        email=data['form'].cleaned_data['email'],
                        password=passwd)
            user.save()
            adr = Address(adr_searchname=data['form'].cleaned_data['searchname'],
                          adr_email=data['form'].cleaned_data['email'],
                          adr_user_id=user,
                          )
            adr.save()
            contacttypes = ContactType.objects.all()
            for ct_type in contacttypes:
                ctdata = ContactData(cd_contacttype_id=ct_type,
                                     cd_textfield=data['form'].cleaned_data['{index}'.format(index=ct_type.id)],
                                     cd_address_id=adr)
                ctdata.save()
            return redirect('proj_contacts')
    else:
        data['form'] = ContactForm()
    print data
    return render(request, template, data)


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
        return redirect('all_contacts')
    else:
        adr = get_object_or_404(Address, pk=address_id)
        datadict = {'searchname': adr.adr_searchname, 'email': adr.adr_email}
        adr_data = ContactData.objects.filter(cd_address_id=address_id).order_by('cd_contacttype_id__ct_sort_id')
        for adr_element in adr_data:
            datadict['{index}'.format(index=adr_element.cd_contacttype_id.id)] = adr_element.cd_textfield
        form = ContactForm(initial=datadict) # TODO: datadict index out of contacttype_id and catagory_id for Tab's
        # or send filtered by category and ordered and give a list with the stop-point
    return render(request, 'contacts/edit_contact.html', {'address': adr, 'message': message, 'form': form, 'categories': categories})


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