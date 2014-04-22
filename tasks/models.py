from django.db import models
from docs.models import Doc
from contacts.models import Address, ContactType
from django.contrib.auth.models import User, Group
from tinymce.models import HTMLField



# Create your models here.


class AuthoriseStruct(models.Model):
    """
    Authorise Structure
    who must sign the task so it is done and where it is shown how
    ---- outdated replaced by Donelist and DonelistLayer in projects/models
    TODO: Delete this
    """
    as_name = models.CharField(verbose_name=u'Name', max_length=100)
    as_info = models.CharField(verbose_name=u'Info', max_length=250, blank=True)
    as_user1_id = models.ForeignKey(User, related_name='as_user1_id')
    as_user1_level = models.IntegerField(blank=True, null=True)
    as_u1_name = models.CharField(verbose_name=u'L1 Name', max_length=100, blank=True)
    as_user2_id = models.ForeignKey(User, related_name='as_user2_id', blank=True, null=True)
    as_user2_level = models.IntegerField(blank=True, null=True)
    as_u2_name = models.CharField(verbose_name=u'L2 Name', max_length=100, blank=True)
    as_user3_id = models.ForeignKey(User, related_name='as_user3_id', blank=True, null=True)
    as_user3_level = models.IntegerField(blank=True, null=True)
    as_u3_name = models.CharField(verbose_name=u'L3 Name', max_length=100, blank=True)
    as_user4_id = models.ForeignKey(User, related_name='as_user4_id', blank=True, null=True)
    as_user4_level = models.IntegerField(blank=True, null=True)
    as_u4_name = models.CharField(verbose_name=u'L4 Name', max_length=100, blank=True)

    def __unicode__(self):
        return self.as_name


class ImmoGroup(models.Model):
    """
    ImmoGroup for Administration Rights on a Variaty of Projects
    """
    ig_name = models.CharField(verbose_name=u'Name', max_length='50')
    ig_created = models.DateTimeField(verbose_name=u'Erstellt', editable=False, auto_now_add=True)
    ig_offdate = models.DateTimeField(verbose_name=u'Last Edit', editable=False, auto_now=True)
    ig_isoff = models.BooleanField(verbose_name=u'entfernt', default=False)
    ig_hide = models.BooleanField(verbose_name=u'nicht Anzeigen', default=False)
    ig_user = models.ForeignKey(User, verbose_name=u'Ersteller', default=User)

    class Meta:
        verbose_name = u'ImmoGroup'
        verbose_name_plural = u'ImmoGroups'
        ordering = ['ig_name']

    def __unicode__(self):
        return self.ig_name


class TaskType(models.Model):
    """
    Tasks Types
    like advice, message, note, report

    ProjTaskType in projects.models need an add by new TaskType
    """
    tt_name = models.CharField(verbose_name=u'Name', max_length=100)
    tt_info = models.CharField(verbose_name=u'Info', max_length=250, blank=True)
    tt_template = models.CharField(max_length=50, verbose_name=u'Template-Name') # for Printlayout
    #tt_templatefile = models.FileField(upload_to="tasktypes/", verbose_name=u'Template-Datei') # TODO: All in one Dir? > Grouped?
    tt_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=u'Erstellt')
    tt_offdate = models.DateTimeField(auto_now=True, editable=False, verbose_name=u'Last Edit')
    tt_isoff = models.BooleanField(default=False, verbose_name=u'entfernt')
    tt_hide = models.BooleanField(default=False, verbose_name=u'verbergen')
    tt_group = models.ForeignKey(ImmoGroup, verbose_name=u'Gruppe')
    tt_parent = models.ForeignKey('TaskType', blank=True, null=True, verbose_name=u'Parent') # for History

    def __unicode__(self):
        return self.tt_name


class ImmoGroupMember(models.Model):
    """
    ImmoGroupMember more in ImmoGroup Class
    - Rights -
    1 = Admin: Manager + Add Manager and Add Admin
    2 = Manager: Member + Add Member and Guests + Edit Group-TaskTypes + Edit Group-ProjTopology
    3 = Member: Guest + Add Project, is Member of all Group Projects
    4 = Guest: is Guest of all Group-Projects, just Look at and manage gotten Tasks
    Guest must be User
    """
    RIGHTS_CHOICES = (
        (1, 'Admin'),
        (2, 'Manager'),
        (3, 'Member'),
        (4, 'Guest'),
    )

    igm_user = models.ForeignKey(User, related_name=u'Ersteller', default=User)
    igm_right = models.IntegerField(max_length=1, default=4, verbose_name=u'Gruppenrecht', choices=RIGHTS_CHOICES)
    igm_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=u'Erstellt')
    igm_offdate = models.DateTimeField(auto_now=True, editable=False, verbose_name=u'last Edit')
    igm_isoff = models.BooleanField(verbose_name=u'entfernt', default=False) # TODO: Editable False and setTrue by Del

    class Meta:
        verbose_name = u'ImmoGroupMember'
        verbose_name_plural = u'ImmoGroupMembers'
        ordering = ['igm_user']

    def __unicode__(self):
        return self.igm_user.get_username()


class Task(models.Model):
    """
    Tasks
    """
    ta_shorttxt = models.CharField(verbose_name=u'Kurztext', max_length=250)
    ta_longtxt = HTMLField(verbose_name=u'Meldungstext', blank= True)
    ta_date = models.DateTimeField(verbose_name=u'Erstellt', editable=False, auto_now_add=True) # for first edit TODO: auto set Date
    ta_editor = models.ForeignKey(User, verbose_name=u'Ersteller', default=User)
    ta_begin = models.DateField(verbose_name=u'Begin', blank=True, null=True)
    ta_begintime = models.TimeField(verbose_name=u'Startzeitpunkt', blank=True, null=True)
    ta_end = models.DateField(verbose_name=u'End', blank=True, null=True)
    ta_endtime = models.TimeField(verbose_name=u'Endzeitpunkt', blank=True, null=True)
    ta_warn = models.DateField(verbose_name=u'Warnen', blank=True, null=True)
    ta_priority = models.IntegerField(blank=True)
    ta_adrid_from = models.ForeignKey(Address, related_name=u'Task-From')  # External
    ta_adrid_to = models.ForeignKey(Address, related_name=u'Task-To')  # Internal
    ta_tasktype = models.ForeignKey(TaskType, verbose_name=u'Meldungstyp')
    ta_parent = models.ForeignKey('Task', blank=True, null=True, related_name=u'Parent')

    def __unicode__(self):
        infotxt = str(self.id) + " | " + str(self.ta_shorttxt)
        return infotxt


class TaskDoc(models.Model):
    """
    Task Documents
    join to Docs App
    """
    td_taksid = models.ForeignKey(Task)
    td_docid = models.ForeignKey(Doc)
    td_info = models.CharField(verbose_name=u'Info', max_length=250)

    def __unicode__(self):
        return self.td_info


class TaskTemplateFields(models.Model):
    """
    Matching Address_Data Types to Print Template Layoutfields
    TODO: autogenerate this from DB
    """
    ttf_company = models.ForeignKey(ContactType, related_name=u'Firma', verbose_name=u'Firma')
    ttf_name = models.ForeignKey(ContactType, related_name=u'Name', verbose_name=u'Name')
    ttf_form_of_adr = models.ForeignKey(ContactType, related_name=u'Anrede', verbose_name=u'Anrede')
    ttf_zipcode = models.ForeignKey(ContactType, related_name=u'PLZ', verbose_name=u'PLZ')
    ttf_streat = models.ForeignKey(ContactType, related_name=u'Strasse', verbose_name=u'Strasse')
    ttf_city = models.ForeignKey(ContactType, related_name=u'Stadt', verbose_name=u'Stadt')
    ttf_postboxzip = models.ForeignKey(ContactType, related_name=u'PLZ_Postbox', verbose_name=u'PLZ Postbox')
    ttf_postbox_city = models.ForeignKey(ContactType, related_name=u'Postfach_Stadt', verbose_name=u'Postfach Stadt')
    ttf_postboxcode = models.ForeignKey(ContactType, related_name=u'Postfach_Nr', verbose_name=u'Postfach Nr')
    ttf_country = models.ForeignKey(ContactType, related_name=u'Land', verbose_name=u'Land')
    ttf_fax = models.ForeignKey(ContactType, related_name=u'Fax', verbose_name=u'Fax')


class TaskTypePattern(models.Model):
    """
    TaskTypePattern Choice for Project add
    """

    ttp_name = models.CharField(max_length=50, verbose_name=u'Bezeichnung')
    ttp_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=u'Erstellt')
    ttp_offdate = models.DateTimeField(auto_now=True, editable=False, verbose_name=u'Last Edit')
    ttp_isoff = models.BooleanField(default=False, verbose_name=u'entfernt')
    ttp_group = models.ForeignKey(ImmoGroup, related_name=u'Gruppenrecht')
    ttp_user = models.ForeignKey(User, editable=False, verbose_name=u'Ersteller', default=User)

    class Meta:
        verbose_name = u'TaskTypePattern'
        verbose_name_plural = u'TaskTypePatterns'
        #ordering = ['']

    def __unicode__(self):
        return self.ttp_name


class TaskTypePatternList(models.Model):
    """
    TaskTypePatternList join by Class TaskTypePattern

    For give a New Project a TaskType Pattern
    """
    ttpl_name = models.CharField(max_length=50, verbose_name=u'Bezeichnung')
    ttpl_user = models.ForeignKey(User, related_name=u'TaskTypePattErsteller', default=User, editable=False)
    ttpl_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=u'Erstellt')
    ttpl_offdate = models.DateTimeField(auto_now=True, editable=False, verbose_name=u'Last Edit')
    ttpl_parent = models.ForeignKey('TaskTypePatternList', blank=True, null=True, related_name='Parent')
    ttpl_isof = models.BooleanField(default=False, verbose_name=u'entfernt')
    ttpl_hide = models.BooleanField(default=False, verbose_name=u'verbergen')
    ttpl_goup = models.ForeignKey(ImmoGroup, verbose_name=u'Gruppenrecht')
    ttpl_pattern = models.ForeignKey(TaskTypePattern, related_name=u'TaskType Pattern')

    class Meta:
        verbose_name = u'TaskTypePatternList'
        verbose_name_plural = u'TaskTypePatternLists'
        ordering = ['ttpl_name']

    def __unicode__(self):
        return self.ttpl_name


