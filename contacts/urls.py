from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # URL for contact in Detail
    url(r'^(?P<item_id>\d+)/$', 'contacts.views.index', name='contact_detail'),
)
