__author__ = 'oerb'

from django.contrib import admin
from menues.models import Menu, Image, MetaInfos
from django.contrib.sites.models import Site
from usrsettings.models import Setting
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class SettingInline(admin.StackedInline):
    model = Setting
    can_delete = False
    verbose_name_plural = 'Setting'


class UserAdmin(UserAdmin):
    inlines = (SettingInline, )


class MenuAdmin(admin.ModelAdmin):
    """
    For nice Menu
    """
    list_display = ('subject', 'parent', 'level', 'menu_hide')
    list_filter = ('menu_hide', 'level')
    search_fields = ('subject',)


class MetaInfosAdmin(admin.ModelAdmin):
    """
    For nice Menu
    """
    list_display = ('metainfo_subject', 'metainfo')


class ImageAdmin(admin.ModelAdmin):
    """
    For nice Menu
    """
    list_display = ('image_subject', 'image_file')
    search_fields = ('image_subject', 'image_file')


# Registrationpart
admin.site.register(Menu, MenuAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(MetaInfos, MetaInfosAdmin)
# Unregister the Site module because Multiple Domain is not implemented
admin.site.unregister(Site)
# Register User Extension Setting.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

