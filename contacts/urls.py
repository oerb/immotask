from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # URL for contact in Detail

    url(r'^(?P<address_id>\d+)/(?P<category_id>\d+)/$', 'contacts.views.ct_detail_tab', name='contact_detailtab'),
    url(r'^view/$', 'contacts.views.proj_contacts', name='proj_contacts'),
    url(r'^view/all/$', 'contacts.views.all_contacts', name='all_contacts'),
    url(r'^new/$', 'contacts.views.new_contact', name='new_contact'),
    url(r'^projadr/(?P<adr_id>\d+)$', 'contacts.views.proj_to_address', name='add_projadr'),
    url(r'^edit/(?P<address_id>\d+)$', 'contacts.views.edit_contact', name='edit_contact'),
    url(r'^test/$', 'contacts.views.test', name="ct_test")
)
