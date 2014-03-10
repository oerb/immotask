from django.db import models
from contacts.models import Address
from menues.models import Image
# Create your models here.


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


class ProjDoc(models.Model):
    """
    Project Documents
    contains a join to the docs app
    """
    pd_projid = models.ForeignKey(Project)
    # pd_docid = models.ForeignKey(Doc) TODO: sign after Doc Apps Model is developed


class Project(models.Model):
    """
    Projects
    central Order ID for structuring Adresses, Documents, Tasks
    in to Projekt-Elements like Houses, Rooms, development etc.
    """
    pro_name = models.CharField(verbose_name=u'Name', max_length=250)
    pro_info = models.CharField(verbose_name=u'Info', max_length=250, blank=True)
    pro_date = models.DateField(verbose_name=u'Erstellt')
    pro_hide = models.BooleanField() # TODO: Standardwert True
    pro_done_date = models.DateTimeField( blank=True)


class ProjDataLayer(models.Model):
    """
    Projects Data Layer
    like Architekt, Country, Projekt Owner etc.
    """
    pdl_name = models.CharField(verbose_name=u'Name', max_length='100')
    pdl_info = models.CharField(verbose_name=u'Info', max_length='250', blank=True)
    pdl_sortid = models.IntegerField(verbose_name=u'Sort Order', blank=True)


class ProjTask(models.Model):
    """
    Projekt Tasks
    join to Tasks app
    """
    pass

    # pt_task_id = modler.ForeignKey(Task) TODO: after Task app is modeled



class ProjStruct(modelsModel):
    """
    Project Structure
    For structuring the Project
        like House, Room, Development, Basement etc. ...
    """
    ps_sortid = models.IntegerField(blank=True)
    ps_name = models.CharField(verbose_name=u'Name', max_length=100)
    ps_imgid = models.ForeignKey(Image, blank=True)  # For Images infront of the Trea


class ProjData(models.Model):
    """
    Project Data
    like, Start, End, Objekt, Streat, Architekt ...
    """
    proj_text = models.CharField(verbose_name=u'Text', max_length=250)
    proj_double = models.DecimalField(verbose_name=u'Dezimalfeld', max_length=250)
    proj_unit = models.CharField(verbose_name=u'Einheit', max_length=20)
