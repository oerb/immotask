#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Data Models for the Main Menu
and some Core Data like the meta-HtmlTags
"""
__author__ = "oerb"
__copyright__ = "GPL 2014"
__license__ = "GPL3"

from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User, Group
from django.utils.timezone import now

class Image(models.Model):
    """
    Class for Images to Populate and Upload
    """
    image_subject = models.CharField(max_length=100, verbose_name=u'Subject')
    image_file = models.ImageField(upload_to="img/")

    class Meta:
        verbose_name = u'Image'
        verbose_name_plural = u'Images'

    def __unicode__(self):
        return  self.image_subject

class Menu(models.Model):
    """
    Homepage Menu
    """
    subject = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    level = models.PositiveIntegerField()
    parent = models.ForeignKey('self', blank=True, null=True,
                             related_name=u'Parent')
    menu_hide = models.BooleanField()
    date_creation = models.DateTimeField(editable=False, auto_now_add=True)
    date_last_edit = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        verbose_name = u'Menu'
        verbose_name_plural = u'Menu'
        ordering = ['-date_creation']

    def __unicode__(self):
        if self.level == 2:
            subjectleveld = str(self.parent) + " | " + self.subject
        else:
            subjectleveld = self.subject
        return subjectleveld


class MetaInfos(models.Model):
    """
    Class for Methatags, Impressum else
    """
    metainfo_subject = models.CharField(max_length=255, verbose_name=u'Subject',
                                         help_text=u'Implemented Tags: impressum, keywords, description, '
                                                   u'author, footer, blogname')
    # metainfo_html = HTMLField(verbose_name=u'Html-Field', blank=True, null=True)
    metainfo = models.TextField(verbose_name=u'Metainfo',blank=True, null=True)

    class Meta:
        verbose_name = u'Meta Info'
        verbose_name_plural = u'Meta Infos'

    def __unicode__(self):
        return self.metainfo_subject