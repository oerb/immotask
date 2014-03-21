from django.db import models
from projects.models import Project
from contacts.models import Address
from django.contrib.auth.models import User, Group


# Create your models here.


class Setting(models.Model):
    """
    User Settings like current Project etc.
    """
    se_current_proj = models.ForeignKey(Project, verbose_name=u'current Project ID',
                                        related_name=u'current Project ID',
                                        blank=True, null=True)
    se_mailwarn = models.BooleanField(verbose_name=u'get Mail warnings')
    se_newtaskmail = models.BooleanField(verbose_name=u'get New Tasks as Mail')
    se_address = models.ForeignKey(Address, verbose_name=u'Adresse', blank=True, null=True)
    se_user = models.OneToOneField(User)