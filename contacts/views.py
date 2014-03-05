from contacts.models import Address, Category, ContactType, ContactData, ContactDataFulltext
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def ct_detail(request, address_id):
        address = get_object_or_404(Address, pk=address_id)
        adr_fulltextfields = ContactDataFulltext.objects.filter(cf_address_id=address.id)
        adr_data = ContactData.objects.filter(cd_address_id=address.id).order_by('cd_contacttype_id__ct_sort_id')
        categories = Category.objects.all()
        return render(request, 'contacts/detail.html',{'address': address, 'adr_fulltextfields': adr_fulltextfields,
                                                  'adr_data': adr_data, 'categories': categories})
# TODO: Url, TAB and Item Id using/filtering in template and view
def ct_detail_tab(request, address_id, category_id):
        category_id = int(category_id)
        address = get_object_or_404(Address, pk=address_id)
        adr_fulltextfields = ContactDataFulltext.objects.filter(cf_address_id=address.id)
        adr_data = ContactData.objects.filter(cd_address_id=address.id).order_by('cd_contacttype_id__ct_sort_id')
        categories = Category.objects.all()
        return render(request, 'contacts/detailtab.html', {'address': address, 'adr_fulltextfields': adr_fulltextfields,
                                                  'adr_data': adr_data, 'category_id': category_id, 'categories': categories})
# TODO: Needs to be filtered by project ID, Needs more Addresselements
def proj_contacts(request):
    adr_data = ContactData.objects.all()
    addresses = Address.objects.all()
    return render(request, 'contacts/proj_contacts.html', {'adr_data': adr_data, 'addresses': addresses})
