__author__ = 'oerb'
from django.contrib import admin
from contacts.models import Address, Category, ContactData, ContactDataFulltext, ContactType
from django.contrib.sites.models import Site

class ContactDataAdmin(admin.ModelAdmin):
    """
    For nice Menu
    """
    list_display = ('cd_contacttype_id', 'cd_textfield', 'cd_address_id')
    # list_filter = ('cd_address_id',)
    search_fields = ('cd_address_id__adr_searchname',)

class ContactTypeAdmin(admin.ModelAdmin):
    """
    For nice Menu
    """
    list_display = ('ct_name', 'ct_category_id', 'ct_sort_id')

# Registrationpart
admin.site.register(Address)
admin.site.register(Category)

admin.site.register(ContactDataFulltext)
admin.site.register(ContactData, ContactDataAdmin)

admin.site.register(ContactType, ContactTypeAdmin)