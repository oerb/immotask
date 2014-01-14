from contacts.models import Address, Category, ContactType, CondtactData, ContactDataFulltext
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request, item_id):
        address = get_object_or_404(Address, pk=item_id)
        adr_fulltextfields = ContactDataFulltext.objects.filter(cf_address_id=address.id)
        adr_data = CondtactData.objects.filter(cd_address_id=address.id)
        return render(request, 'contacts/detail.html',{'address':address, 'adr_fulltextfields':adr_fulltextfields,
                                                  'adr_data':adr_data})
