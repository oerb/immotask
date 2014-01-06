# encoding: utf-8

from django.db import models


class Address(models.Model):
    """
    Address Model
    contains just searchname and E-Mail. Rest is configurable by
    Contactdata
    """
    adr_searchname = models.CharField(verbose_name=u'name', max_length=255)
    adr_email = models.CharField(verbose_name=u'E-Mail', max_length=255)  # defined here for special use in sending module

    class Meta:
        verbose_name = u'Adresse'
        verbose_name_plural = u'Adresses'
        ordering = ['shownName']

    def __unicode__(self):
        return self.searchname


class Category(models.Model):
    """
    Category Model
    to categorize adresses in company, personal etc.
    so you could use tabs for organization
    """
    ca_name = models.CharField(verbose_name=u'Name')
    ca_description = models.TextField(verbose_name=u'Description', blank=True)

    class Meta:
        verbose_name = u'category'
        verbose_name_plural = u'categories'

    def __unicode__(self):
        return self.ca_name

class CondtactData(models.Model):
    """
    Contactdata Model
    for phone, fax, email etc.
    """
    cd_contacttype_id = models.ForeignKey(Contacttype)
    cd_textfield = models.CharField(255)
    cd_address_id = models.ForeignKey(Address)

    def __unicode__(self):
        return self.cd_contacttype_id.ct_name


class ContactDataFulltext(models.Model):
    """
    Contactdata Fulltext Model
    for Fulltext elements
    """
    cf_contacttype_id = models.ForeignKey(Contacttype)
    cf_textfield = models.TextField()
    cf_address_id = models.ForeignKey(Address, editable=False)

    def __unicode__(self):
        return self.cf_textfield


class ContactType(models.Model):
    """
    Contacttype Model
    Types like phone, fax, email, etc.
    """
    ct_name = models.CharField(u'name', max_length=20)
    ct_notice = models.CharField(u'notice', max_length=255)
    ct_category_id = models.ForeignKey(Category)

    def __unicode__(self):
        return self.ct_name