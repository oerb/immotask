from django.db import models
from contacts.models import Address
from menues.models import Image
from docs.models import Doc
from tasks.models import Task
# Create your models here.


class Project(models.Model):
    """
    Projects
    central Order ID for structuring Adresses, Documents, Tasks
    in to Projekt-Elements like Houses, Rooms, development etc.
    """
    pro_name = models.CharField(verbose_name=u'Name', max_length=250)
    pro_info = models.CharField(verbose_name=u'Info', max_length=250, blank=True)
    pro_date = models.DateField(verbose_name=u'Erstellt')
    pro_hide = models.BooleanField(verbose_name=u'Hide')  # TODO: Standardwert True
    pro_done_date = models.DateTimeField( blank=True)

    def __unicode__(self):
        return self.pro_name


class ProjAdrTyp(models.Model):
    """
    Projekt Address Types like
    Architekt, Planning, Companies ...
    """
    pat_name = models.CharField(verbose_name=u'Name', max_length=100)
    pat_info = models.CharField(verbose_name=u'Info', max_length=250, blank=True)

    def __unicode__(self):
        return pat_name


class ProjectAddress(models.Model):
    """
    Project Address Model
    contains a join info to the contacts app
    """
    pa_adr_id = models.ForeignKey(Address)
    pa_adrtype = models.ForeignKey(ProjAdrTyp)
    pa_projid = models.ForeignKey(Project)

    def __unicode__(self):
        return self.pa_adr_id.adr_searchname


class ProjDoc(models.Model):
    """
    Project Documents
    contains a join to the docs app
    """
    pd_projid = models.ForeignKey(Project)
    pd_docid = models.ForeignKey(Doc)

    def __unicode__(self):
        return self.pd_docid.doc_subject


class ProjDataLayer(models.Model):
    """
    Projects Data Layer
    like Architekt, Country, Projekt Owner etc.
    """
    pdl_name = models.CharField(verbose_name=u'Name', max_length='100')
    pdl_info = models.CharField(verbose_name=u'Info', max_length='250', blank=True)
    pdl_sortid = models.IntegerField(verbose_name=u'Sort Order', blank=True)

    def __unicode__(self):
        return self.pdl_name


class ProjTask(models.Model):
    """
    Projekt Tasks
    join to Tasks app
    """
    pt_taskid = models.ForeignKey(Task)
    pt_projid = models.ForeignKey(Project)

    def __unicode__(self):
        info = "Projekt: " + str(self.pt_projid.id) + " " + str(self.pt_projid.pro_name) \
               + " TaskID: " + str(self.pt_taskid.id)
        return info


class ProjStruct(models.Model):
    """
    Project Structure
    For structuring the Project
        like House, Room, Development, Basement etc. ...
    """
    ps_sortid = models.IntegerField(blank=True)
    ps_name = models.CharField(verbose_name=u'Name', max_length=100)
    ps_imgid = models.ForeignKey(Image, blank=True)  # For Images infront of the Trea

    def __unicode__(self):
        return self.ps_name


class ProjData(models.Model):
    """
    Project Data
    like, Start, End, Objekt, Architekt ...
    """
    proj_text = models.CharField(verbose_name=u'Text', max_length=250)
    proj_double = models.DecimalField(verbose_name=u'Dezimalfeld', max_digits=15, decimal_places=2)
    proj_unit = models.CharField(verbose_name=u'Einheit', max_length=20)

    def __unicode__(self):
        info = str(self.proj_text) + " " + str(self.proj_double) + " " + str(self.proj_unit)
        return info