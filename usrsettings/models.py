from django.db import models
from projects.models import Project
from contacts.models import Address
from django.contrib.auth.models import User


# Create your models here.


class Setting(models.Model):
    """
    User Settings like current Project etc.
    """
    se_current_proj = models.ForeignKey(Project, verbose_name=u'current Project ID',
                                        related_name=u'current Project ID',
                                        blank=True, null=True)
    se_mailwarn = models.BooleanField(verbose_name=u'get Mail warnings', default=True)
    se_newtaskmail = models.BooleanField(verbose_name=u'get New Tasks as Mail', default=True)
    se_address = models.ForeignKey(Address, verbose_name=u'Adresse', blank=True, null=True)
    se_user = models.OneToOneField(User)

    def __unicode__(self):
        info = str(self.se_current_proj) + " / " + str(self.se_user)
        return info


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
    igm_date = models.DateTimeField(auto_now_add=True, verbose_name=u'Erstellt')
    igm_offdate = models.DateTimeField(auto_now=True, verbose_name=u'last Edit')
    igm_isoff = models.BooleanField(verbose_name=u'entfernt', default=False)

    class Meta:
        verbose_name = u'ImmoGroupMember'
        verbose_name_plural = u'ImmoGroupMembers'
        ordering = ['igm_user']

    def __unicode__(self):
        return self.igm_user.get_username()


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
    RIGHTS_CHOICES = (
        (1, 'Admin'),
        (2, 'Manager'),
        (3, 'Member'),
        (4, 'Guest'),
    )
    pg_user = models.ForeignKey(User, related_name=u'Benutzer')
    pg_date = models.DateTimeField(auto_now_add=True, verbose_name=u'Erstellt')
    pg_offdate = models.DateTimeField(auto_now=Ture, verbose_name=u'Last Edit')
    pg_isoff = models.BooleanField(verbose_name=u'entfernt', default=False)
    pg_right = models.IntegerField(verbose_name=u'Projekt-Recht', choices=RIGHTS_CHOICES, default=4)

    class Meta:
        verbose_name = u'ProjGroup'
        verbose_name_plural = u'ProjGroups'
        ordering = ['pg_user']

    def __unicode__(self):
        return self.pg_user