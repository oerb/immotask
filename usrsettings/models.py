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



