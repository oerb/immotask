from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.


class DocType(models.Model):
    """
    Document Types
    like Word, Excel, Openoffice, CAD, Images ...
    """
    dt_name = models.CharField(verbose_name=u'Name', max_length=100)
    dt_info = models.CharField(verbose_name=u'Info', max_length=250)

    def __unicode__(self):
        return self.dt_name


class Doc(models.Model):
    """
    Documents
    like Word, Excel etc. with History and as Task or with Child tasks
    """
    doc_name = models.CharField(max_length=50, verbose_name=u'Bezeichnung')
    doc_info = models.CharField(max_length=250, verbose_name=u'Info')
    doc_file = models.FileField(upload_to="docs/")
    doc_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=u'Erstellt')
    doc_offdate = models.DateTimeField(auto_now=True, editable=False, verbose_name=u'LastEdit')
    doc_isoff = models.BooleanField(default=False, verbose_name=u'entfernt')
    doc_parent = models.ForeignKey('Doc', related_name=u'Parent')  # for History
    doc_user = models.ForeignKey(User, auto_created=User, editable=False, related_name=u'DocErsteller')
    doc_offuser = models.ForeignKey(User, default=User, editable=False, related_name=u'LetzterBearbeiter')
    # doc_userid = models.ForeignKey() TODO: UserID has to be added

    def __unicode__(self):
        return self.doc_name



