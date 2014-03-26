from django.db import models
from docs.models import Doc
from contacts.models import Address, ContactType
from projects.models import ProjTask, Project
from django.contrib.auth.models import User, Group


# Create your models here.


class AuthoriseStruct(models.Model):
    """
    Authorise Structure
    who must sign the task so it is done and where it is shown how
    ---- outdated replaced by Donelist and DonelistLayer
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
    dl_user_id = models.ForeignKey(User, related_name=u'User')
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

class TaskType(models.Model):
    """
    Tasks Types
    like advice, message, note, report
    """
    tt_name = models.CharField(verbose_name=u'Name', max_length=100)
    tt_info = models.CharField(verbose_name=u'Info', max_length=250, blank=True)
    tt_authstruct_id = models.ForeignKey(AuthoriseStruct)  # For a Structure in Signing the Task to get done
    tt_template = models.CharField(max_length=50, verbose_name=u'Templatename') # for Printlayout

    def __unicode__(self):
        return self.tt_name


class Task(models.Model):
    """
    Tasks
    """
    ta_shorttxt = models.CharField(verbose_name=u'Kurztext', max_length=250)
    ta_longtxt = models.TextField(verbose_name=u'Meldungstext', blank= True)
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

