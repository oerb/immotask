from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # URL for contact in Detail
    url(r'^(?P<address_id>\d+)/$', 'contacts.views.ct_detail', name='contact_detail'),
    url(r'^(?P<address_id>\d+)/(?P<catagory_id>\d+)/$', 'contacts.views.ct_detail_tab', name='contact_detailtab'),
)
