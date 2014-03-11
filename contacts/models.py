# encoding: utf-8

from django.db import models


class Address(models.Model):
    """
    Address Model
    contains just searchname and E-Mail. Rest is configurable by
    Contactdata
    """
    adr_searchname = models.CharField(verbose_name=u'Name', max_length=255)
    adr_email = models.CharField(verbose_name=u'E-Mail', max_length=255)  # defined for special use in sending module

    class Meta:
        verbose_name = u'Adresse'
        verbose_name_plural = u'Adresses'
        ordering = ['adr_searchname']

    def __unicode__(self):
        return self.adr_searchname


class Category(models.Model):
    """
    Category Model
    to categorize adresses in company, personal etc.
    so you could use tabs for organization
    """
    ca_name = models.CharField(verbose_name=u'Name', max_length=255)
    ca_description = models.TextField(verbose_name=u'Description', blank=True)

    class Meta:
        verbose_name = u'Category'
        verbose_name_plural = u'Categories'

    def __unicode__(self):
        return self.ca_name


class ContactType(models.Model):
    """
    Contacttype Model
    Types like phone, fax, email, etc.
    """
    ct_name = models.CharField(verbose_name=u'Name', max_length=20)
    ct_info = models.CharField(verbose_name=u'Notice', max_length=255, blank=True)
    ct_category_id = models.ForeignKey(Category)
    ct_sort_id = models.IntegerField(verbose_name=u'sort_id')

    def __unicode__(self):
        info = str(self.ct_category_id) + " , " + str(self.ct_name)
        return info


class ContactData(models.Model):
    """
    Contactdata Model
    for phone, fax, email etc.
    """
    cd_contacttype_id = models.ForeignKey(ContactType)
    cd_textfield = models.CharField(max_length=255)
    cd_address_id = models.ForeignKey(Address)

    class Meta:
        verbose_name = u'Contact Data'
        verbose_name_plural = u'Contact Data'

    def __unicode__(self):
        return self.cd_contacttype_id.ct_name


class ContactDataFulltext(models.Model):
    """
    Contactdata Fulltext Model
    for Fulltext elements
    """
    cf_contacttype_id = models.ForeignKey(ContactType)
    cf_textfield = models.TextField()
    cf_address_id = models.ForeignKey(Address)

    def __unicode__(self):
        return self.cf_textfield