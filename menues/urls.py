from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Login Forms
    url(r'^login/$', 'menues.views.login_page',
        name="login"),
    url(r'^logout/$', 'menues.views.logout_view',
        name="logout"),
    # Meta Infos etc.
    url(r'^impressum/$', 'menues.views.impressum', name='impressum'),

)
