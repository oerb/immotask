from django.db import models
from contacts.models import Address
from menues.models import Image
from docs.models import Doc
from tasks.models import Task, TaskType, ImmoGroup
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
    pro_hide = models.BooleanField(verbose_name=u'Hide', default=False)
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
        info = "Projekt: " + str(self.pt_projid.id) + " - " + str(self.pt_projid.pro_name) \
               + " TaskID: " + str(self.pt_taskid.id)
        return info


class ProjTaskType(models.Model):
    """
    ProjTaskType for Join to TaskType in tasks.models
    """
    ptty_tasktypeid = models.ForeignKey(TaskType)
    ptty_projectid = models.ForeignKey(Project)

    def __unicode__(self):
        info = "TaskType: " + str(self.ptty_tasktypeid.tt_name) + " / Project: " + str(self.ptty_projectid.pro_name)
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
        (3, 'Level3'),
        (4, 'Level4'),
        (5, 'Level5'),
        (6, 'Level6'),
        (7, 'Level7'),
        (8, 'Level8'),
    )
    dll_tasktype_id = models.ForeignKey(TaskType, related_name=u'TaskType')
    # if Standard = True >> goes over all where no Project Level is defined
    dll_proj_id = models.ForeignKey(Project, related_name=u'Project', null=True, blank=True)
    dll_user_id = models.ForeignKey(User, related_name=u'User')
    dll_level = models.IntegerField(max_length=2, verbose_name=u'Level', choices=LEVEL_CHOICES)
    # if Standard = True >> goes over all where no Project Level is defined
    dll_standard = models.BooleanField(default=True, verbose_name=u'Is Standard')

    def __unicode__(self):
        info = str(self.dll_level) + " / " + str(self.dll_user_id) + " / " + str(self.dll_tasktype_id)
        return info

RIGHTS_CHOICES = (
        (1, 'Admin'),
        (2, 'Manager'),
        (3, 'Member'),
        (4, 'Guest'),
    )

class ProjGroup(models.Model):
    """
    ProjGroup for Rightmanagement in Projects
    - Rights -
    1 = Admin: Manager + Add Manager and Add Admin
    2 = Manager: Member + Add Member and Guests + Edit Project-TaskTypes + Edit Project-Topology
    3 = Member: Guest + Add and Edit Tasks, Documents, Addresses
    4 = Guest: just Look at and manage gotten Tasks, all Guest shown Project Documents, all Addressis - no Edit
    Guest must be User
    """

    pg_user = models.ForeignKey(User, verbose_name=u'Benutzer')
    pg_date = models.DateTimeField(auto_now_add=True, verbose_name=u'Erstellt')
    pg_offdate = models.DateTimeField(auto_now=True, verbose_name=u'Last Edit')
    pg_isoff = models.BooleanField(verbose_name=u'entfernt', default=False)
    pg_right = models.IntegerField(verbose_name=u'Projekt-Recht', choices=RIGHTS_CHOICES, default=4)

    class Meta:
        verbose_name = u'ProjGroup'
        verbose_name_plural = u'ProjGroups'
        # ordering = ['pg_user']

    def __unicode__(self):
        info = str(self.pg_user) + " | " + str(self.pg_right)
        return info


class ProjTopologyPattern(models.Model):
    """
    ProjTopologyPattern for a ProjectTree Pattern
    """
    ptp_name = models.CharField(max_length=50, verbose_name=u'Bezeichnung')
    ptp_info = models.CharField(max_length=250, verbose_name=u'Info')
    ptp_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=u'Erstellt')
    ptp_offdate = models.DateTimeField(auto_now=True, editable=False, verbose_name=u'LastEdit')
    ptp_isoff = models.BooleanField(default=False, verbose_name=u'entfernt')
    ptp_group = models.IntegerField(max_length=2, choices=RIGHTS_CHOICES, verbose_name=u'Gruppe')
    ptp_user = models.ForeignKey(User, default=User, related_name=u'TopoPatternErsteller')

    class Meta:
        verbose_name = u'ProjTopologyPattern'
        verbose_name_plural = u'ProjTopologyPatterns'
        ordering = ['ptp_name']

    def __unicode__(self):
        return self.ptp_name


class ProjTopologyIcons(models.Model):
    """
    ProjTopologyIcons for nice Tree Icons
    """
    pti_name = models.CharField(max_length=50, verbose_name=u'Bezeichnung')
    pti_file = models.ImageField(upload_to='topologyIcons/')
    pti_hide = models.BooleanField(default=False, verbose_name=u'verbergen')

    class Meta:
        verbose_name = u'ProjTopologyIcons'
        verbose_name_plural = u'ProjTopologyIconss'
        ordering = ['pti_name']

    def __unicode__(self):
        return self.pti_name


class ProjTopologyPatternList(models.Model):
    """
    ProjTopologyPatternList for a ProjectTree Pattern
    """
    ptpl_name = models.CharField(max_length=50, verbose_name=u'Bezeichnung')
    ptpl_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=u'Erstellt')
    ptpl_offdate = models.DateTimeField(auto_now=True, editable=False, verbose_name=u'LastEdit')
    ptpl_isoff = models.BooleanField(default=False, verbose_name=u'entfernt')
    ptpl_group = models.IntegerField(max_length=2,choices=RIGHTS_CHOICES, verbose_name=u'Projekt-Gruppe')
    ptpl_user = models.ForeignKey(User, default=User, related_name=u'TopoPatListErsteller')
    ptpl_parent = models.ForeignKey('ProjTopologyPatternList', verbose_name=u'Parent', blank=True, null=True)
    ptpl_icon = models.ForeignKey(ProjTopologyIcons, verbose_name=u'Tree Icon', default=1)
    ptpl_pattern = models.ForeignKey(ProjTopologyPattern, verbose_name=u'TreePattern')
    ptpl_orderid = models.IntegerField(max_length=5, verbose_name=u'Sortierreihenfolge')

    class Meta:
        verbose_name = u'ProjTopologyPatternList'
        verbose_name_plural = u'ProjTopologyPatternLists'
        ordering = ['ptpl_name']

    def __unicode__(self):
        return self.ptpl_name


class ProjTopology(models.Model):
    """
    ProjTopology for Project Tree
    """
    pt_name = models.CharField(max_length=50, verbose_name=u'Bezeichnung')
    pt_parent = models.ForeignKey('ProjTopology', verbose_name=u'Parent', null=True, blank=True)
    pt_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=u'Erstellt')
    pt_offdate = models.DateTimeField(auto_now=True, editable=False, verbose_name=u'LastEdit')
    pt_isoff = models.BooleanField(default=False, verbose_name=u'entfernt')
    pt_group = models.IntegerField(max_length=2, choices=RIGHTS_CHOICES, verbose_name=u'Projekt-Gruppe')
    pt_user = models.ForeignKey(User, default=User, related_name=u'TopologyErsteller')
    pt_icon = models.ForeignKey(ProjTopologyIcons, verbose_name=u'Tree Icon', default=1)
    pt_orderid = models.IntegerField(max_length=5, verbose_name=u'Sortierreihenfolge')
    pt_proj = models.ForeignKey(Project, verbose_name=u'Projekt')

    class Meta:
        verbose_name = u'ProjTopology'
        verbose_name_plural = u'ProjTopologys'
        #ordering = ['pt_order_id']

    def __unicode__(self):
        return self.pt_name


class DocSticker(models.Model):
    """
    DocSticker for stick Doc to ProjTopology, Address or Task
    """
    dst_doc = models.ForeignKey(Doc, verbose_name=u'Dokument')
    dst_adr = models.ForeignKey(Address, verbose_name=u'Adresse', blank=True, null=True)
    dst_projtopology = models.ForeignKey(ProjTopology, verbose_name=u'Projekt Treenode', blank=True, null=True)
    dst_task = models.ForeignKey(Task, verbose_name=u'Aufgabe', blank=True, null=True)

    class Meta:
        verbose_name = u'DocSticker'
        verbose_name_plural = u'DocStickers'
        ordering = ['dst_doc']

    def __unicode__(self):
        return self.dst_doc