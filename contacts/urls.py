from django.conf.urls import patterns, include, url
from .views import proj_to_address, edit_contact, all_contacts, proj_contacts, ct_detail_tab, new_contact

urlpatterns = patterns('',
    # URL for contact in Detail

    url(r'^(?P<address_id>\d+)/(?P<category_id>\d+)/$', ct_detail_tab, name='contact_detailtab'),
    url(r'^view/$', proj_contacts, name='proj_contacts'),
    url(r'^view/all/$', all_contacts, name='all_contacts'),
    url(r'^new/$', new_contact, name='new_contact'),
    url(r'^projadr/(?P<adr_id>\d+)$', proj_to_address, name='add_projadr'),
    url(r'^edit/(?P<address_id>\d+)$', edit_contact, name='edit_contact'),
)
