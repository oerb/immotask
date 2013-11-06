# encoding: utf-8

from django.db import models


class Address(models.Model):
    """
    Address Model
    contains all Addresses central. In Category it will be split into
    Company, etc.
    """
    name = models.CharField(u'name', max_length=255)
    first_name = models.CharField(u'first name', max_length=255)
    shownName = models.CharField(u'shown name', max_length=255)
    company = models.CharField(u'company', max_length=255)
    street = models.CharField(u'street', max_length=255)
    postal_code = models.CharField(u'postal code', max_length=20)
    city = models.CharField(u'city', max_length=255)
    country = models.CharField(u'country', max_length=255)
    url = models.CharField(u'URL', max_length=255)
    email = models.CharField(u'E-Mail', max_length=255)  # defined here for special use in sending module
    fax = models.CharField(u'Fax', max_length=255)  # defined here for special use in sending module
    position = models.CharField(u'position', max_length=255)
    department = models.CharField(u'department', max_length=255)  # Abteilung
    category = models.ForeignKey(Category, editable=False)  # Company, Person, free...
    freetext = models.TextField(u'freetext', blank=True)

    class Meta:
        verbose_name = u'adresse'
        verbose_name_plural = u'adresses'
        ordering = ['shownName']


class Category(models.Model):
    """
    Category Model
    to categorize adresses in company, person etc.
    """
    name = models.CharField(u'Name')
    description = models.TextField(u'description', blank=True)

    class Meta:
        verbose_name = u'category'
        verbose_name_plural = u'categories'


class Condtactdata(models.Model):
    """
    Contactdata Model
    for phone, fax, email etc.
    """
    contacttype = models.ForeignKey(Contacttype, editable=False)
    contact = models.CharField(255)
    address = models.ForeignKey(Address, editable=False)

class Contacttype(models.Model):
    """
    Contacttype Model
    Types like phone, fax, email, etc.
    """
    name = models.CharField(u'name', max_length=20)
    notice = models.CharField(u'notice', max_length=255)

