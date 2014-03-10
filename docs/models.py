from django.db import models

# Create your models here.


class DocType(models.Model):
    """
    Document Types
    like Word, Excel, Openoffice, CAD, Images ...
    """
    dt_name = models.CharField(verbose_name=u'Name', max_length=100)
    dt_info = models.CharField(verbose_name=u'Info', max_length=250)

class Doc(models.Model):
    """
    Documents
    like Word, Excel etc. with History and as Task or with Child tasks
    """
    doc_subject = models.CharField(max_length=100, verbose_name=u'Subject')
    doc_file = models.FileField(upload_to="docs/")
    # doc_userid = models.ForeignKey() TODO: UserID has to be added
