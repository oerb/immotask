from django.db import models
from contacts.models import Address
from menues.models import Image
from docs.models import Doc
from tasks.models import Task, TaskType
from django.contrib.auth.models import User, Group


class Project(models.Model):
    """
    Projects
    central Order ID for structuring Adresses, Documents, Tasks
    in to Projekt-Elements like Houses, Rooms, development etc.
    """
    pro_name = models.CharField(verbose_name=u'Name', max_length=40)
    pro_info = models.CharField(verbose_name=u'Info', max_length=250, blank=True)
    pro_date = models.DateField(verbose_name=u'Erstellt', editable=False, auto_now_add=True)
    pro_hide = models.BooleanField(verbose_name=u'Hide', default=False)  # TODO: Standardwert True
    pro_done_date = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.pro_name


class ProjAdrTyp(models.Model):
    """
    Project Address Types like
    Architect Planning, Companies ...
    """
    pat_name = models.CharField(unique=True, verbose_name=u'Name', max_length=30)
    pat_info = models.CharField(verbose_name=u'Info', max_length=250, blank=True)

    def __unicode__(self):
        info = self.pat_name + " / " + self.pat_info
        return info


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
    like Architect, Country, Projekt Owner etc.
    """
    pdl_name = models.CharField(verbose_name=u'Name', max_length='100')
    pdl_info = models.CharField(verbose_name=u'Info', max_length='250', blank=True)
    pdl_sortid = models.IntegerField(verbose_name=u'Sort Order', blank=True)

    def __unicode__(self):
        return self.pdl_name


class ProjTask(models.Model):
    """
    Project Tasks
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
    ps_imgid = models.ForeignKey(Image, blank=True, null=True)  # For Images infront of the Trea
    ps_parent = models.ForeignKey('self', blank=True, null=True, related_name=u'Parent')

    def __unicode__(self):
        return self.ps_name


class ProjData(models.Model):
    """
    Project Data
    like, Start, End, Objekt, Architekt Porject Saldo...
    """
    proj_id = models.ForeignKey(Project)
    proj_datalayer_id = models.ForeignKey(ProjDataLayer)
    proj_text = models.CharField(verbose_name=u'Text', max_length=250)
    proj_double = models.DecimalField(verbose_name=u'Dezimalfeld', max_digits=15, decimal_places=2)
    proj_unit = models.CharField(verbose_name=u'Einheit', max_length=20)

    def __unicode__(self):
        info = str(self.proj_text) + " " + str(self.proj_double) + " " + str(self.proj_unit)
        return info


class Donelist(models.Model):
    """
    Contains the Done behavior for Tasks with Authorization Level
    """
    LEVEL_CHOICES = (
        (1, 'Level1'),
        (2, 'Level2'),
        (3, 'Level3'),
        (4, 'Level4'),
        (5, 'Level5'),
        (6, 'Level6'),
        (7, 'Level7'),
        (8, 'Level8'),
    )
    dl_projtask_id = models.ForeignKey(ProjTask, related_name=u'ProjectTask')
    dl_user_id = models.ForeignKey(User, related_name=u'User_id')
    dl_level = models. IntegerField(max_length=2, verbose_name=u'Level', choices=LEVEL_CHOICES)
    dl_done = models.BooleanField(default=False, verbose_name=u'Done')
    dl_date = models.DateTimeField(auto_now=True, verbose_name=u'Done Date')

    def __unicode__(self):
        info = str(self.dl_user_id) + " / " + str(self.dl_projtask_id)
        return info


class DonelistLayer(models.Model):
    """
    Contains the Authorization Level for Donelist
    ( when not in Logic TASK_To and TASK_From )
    """
    LEVEL_CHOICES = (
        (1, 'Level1'),
        (2, 'Level2'),
        (3, 'Level3'),
        (4, 'Level4'),
        (5, 'Level5'),
        (6, 'Level6'),
        (7, 'Level7'),
        (8, 'Level8'),
    )
    dll_tasktype_id = models.ForeignKey(TaskType, related_name=u'TaskType')
    dll_proj_id = models.ForeignKey(Project, related_name=u'Project')
    dll_user_id = models.ForeignKey(User, related_name=u'User')
    dll_level = models.IntegerField(max_length=2, verbose_name=u'Level', choices=LEVEL_CHOICES)
    dll_standard = models.BooleanField(default=True, verbose_name=u'Is Standard')

    def __unicode__(self):
        info = str(self.dll_level) + " / " + str(self.dll_user_id) + " / " + str(self.dll_tasktype_id)
        return info