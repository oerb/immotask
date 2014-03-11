from django.db import models
from docs.models import Doc
from contacts.models import Address
from django.contrib.auth.models import User, Group

# Create your models here.


class AuthoriseStruct(models.Model):
    """
    Authorise Structure
    who must sign the task so it is done and where it is shown how
    """
    as_name = models.CharField(verbose_name=u'Name', max_length=100)
    as_info = models.CharField(verbose_name=u'Info', max_length=250, blank=True)
    # as_user1_id = models.ForeignKey(User) TODO: Userid add
    as_user1_level = models.IntegerField(blank=True, null=True)
    as_u1_name = models.CharField(verbose_name=u'L1 Name', max_length=100, blank=True)
    # as_user2_id = models.ForeignKey(User) TODO: Userid add
    as_user2_level = models.IntegerField(blank=True, null=True)
    as_u2_name = models.CharField(verbose_name=u'L2 Name', max_length=100, blank=True)
    # as_user3_id = models.ForeignKey(User) TODO: Userid add
    as_user3_level = models.IntegerField(blank=True, null=True)
    as_u3_name = models.CharField(verbose_name=u'L3 Name', max_length=100, blank=True)
    # as_user4_id = models.ForeignKey(User) TODO: Userid add
    as_user4_level = models.IntegerField(blank=True, null=True)
    as_u4_name = models.CharField(verbose_name=u'L4 Name', max_length=100, blank=True)

    def __unicode__(self):
        return self.as_name


class TaskType(models.Model):
    """
    Tasks Types
    like advice, message, note, report
    """
    tt_name = models.CharField(verbose_name=u'Name', max_length=100)
    tt_info = models.CharField(verbose_name=u'Info', max_length=250, blank=True)
    tt_authstruct_id = models.ForeignKey(AuthoriseStruct)  # For a Structure in Signing the Task to get done

    def __unicode__(self):
        return self.tt_name


class Task(models.Model):
    """
    Tasks
    """
    ta_shorttxt = models.CharField(verbose_name=u'Kurztext', max_length=250)
    ta_longtxt = models.TextField(verbose_name=u'Meldungstext', blank= True)
    ta_date = models.DateTimeField(verbose_name=u'Erstellt',auto_now_add=True) # for first edit TODO: auto set Date
    ta_editor = models.ForeignKey(User)
    ta_begin = models.DateTimeField(verbose_name=u'Begin', blank=True, null=True)
    ta_end = models.DateTimeField(verbose_name=u'End', blank=True, null=True)
    ta_warn = models.DateField(verbose_name=u'Warnen', blank=True, null=True)
    ta_priority = models.IntegerField(blank=True)
    ta_adrid_from = models.ForeignKey(Address)  # External
    ta_adrid_to = models.ForeignKey(Address)  # Internal TODO: Userid ADD
    ta_tasktype = models.ForeignKey(TaskType)
    # ta_parent = models.ForeignKey(self, blank=True) TODO: Self ForeignKey ...

    def __unicode__(self):
        return self.ta_shorttxt


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