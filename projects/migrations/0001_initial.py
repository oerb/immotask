# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'projects_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pro_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('pro_info', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('pro_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('pro_hide', self.gf('django.db.models.fields.BooleanField')()),
            ('pro_done_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'projects', ['Project'])

        # Adding model 'ProjAdrTyp'
        db.create_table(u'projects_projadrtyp', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pat_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('pat_info', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
        ))
        db.send_create_signal(u'projects', ['ProjAdrTyp'])

        # Adding model 'ProjectAddress'
        db.create_table(u'projects_projectaddress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pa_adr_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Address'])),
            ('pa_adrtype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.ProjAdrTyp'])),
            ('pa_projid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Project'])),
        ))
        db.send_create_signal(u'projects', ['ProjectAddress'])

        # Adding model 'ProjDoc'
        db.create_table(u'projects_projdoc', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pd_projid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Project'])),
            ('pd_docid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['docs.Doc'])),
        ))
        db.send_create_signal(u'projects', ['ProjDoc'])

        # Adding model 'ProjDataLayer'
        db.create_table(u'projects_projdatalayer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pdl_name', self.gf('django.db.models.fields.CharField')(max_length='100')),
            ('pdl_info', self.gf('django.db.models.fields.CharField')(max_length='250', blank=True)),
            ('pdl_sortid', self.gf('django.db.models.fields.IntegerField')(blank=True)),
        ))
        db.send_create_signal(u'projects', ['ProjDataLayer'])

        # Adding model 'ProjTask'
        db.create_table(u'projects_projtask', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pt_taskid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tasks.Task'])),
            ('pt_projid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Project'])),
        ))
        db.send_create_signal(u'projects', ['ProjTask'])

        # Adding model 'ProjStruct'
        db.create_table(u'projects_projstruct', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ps_sortid', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('ps_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ps_imgid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['menues.Image'], null=True, blank=True)),
            ('ps_parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'Parent', null=True, to=orm['projects.ProjStruct'])),
        ))
        db.send_create_signal(u'projects', ['ProjStruct'])

        # Adding model 'ProjData'
        db.create_table(u'projects_projdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('proj_text', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('proj_double', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('proj_unit', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'projects', ['ProjData'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'projects_project')

        # Deleting model 'ProjAdrTyp'
        db.delete_table(u'projects_projadrtyp')

        # Deleting model 'ProjectAddress'
        db.delete_table(u'projects_projectaddress')

        # Deleting model 'ProjDoc'
        db.delete_table(u'projects_projdoc')

        # Deleting model 'ProjDataLayer'
        db.delete_table(u'projects_projdatalayer')

        # Deleting model 'ProjTask'
        db.delete_table(u'projects_projtask')

        # Deleting model 'ProjStruct'
        db.delete_table(u'projects_projstruct')

        # Deleting model 'ProjData'
        db.delete_table(u'projects_projdata')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contacts.address': {
            'Meta': {'ordering': "['adr_searchname']", 'object_name': 'Address'},
            'adr_email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'adr_searchname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'docs.doc': {
            'Meta': {'object_name': 'Doc'},
            'doc_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'doc_subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'menues.image': {
            'Meta': {'object_name': 'Image'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image_subject': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'projects.projadrtyp': {
            'Meta': {'object_name': 'ProjAdrTyp'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pat_info': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'pat_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'projects.projdata': {
            'Meta': {'object_name': 'ProjData'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proj_double': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'proj_text': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'proj_unit': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'projects.projdatalayer': {
            'Meta': {'object_name': 'ProjDataLayer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pdl_info': ('django.db.models.fields.CharField', [], {'max_length': "'250'", 'blank': 'True'}),
            'pdl_name': ('django.db.models.fields.CharField', [], {'max_length': "'100'"}),
            'pdl_sortid': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
        },
        u'projects.projdoc': {
            'Meta': {'object_name': 'ProjDoc'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pd_docid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['docs.Doc']"}),
            'pd_projid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Project']"})
        },
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pro_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'pro_done_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pro_hide': ('django.db.models.fields.BooleanField', [], {}),
            'pro_info': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'pro_name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'projects.projectaddress': {
            'Meta': {'object_name': 'ProjectAddress'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pa_adr_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Address']"}),
            'pa_adrtype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.ProjAdrTyp']"}),
            'pa_projid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Project']"})
        },
        u'projects.projstruct': {
            'Meta': {'object_name': 'ProjStruct'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ps_imgid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['menues.Image']", 'null': 'True', 'blank': 'True'}),
            'ps_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ps_parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'Parent'", 'null': 'True', 'to': u"orm['projects.ProjStruct']"}),
            'ps_sortid': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
        },
        u'projects.projtask': {
            'Meta': {'object_name': 'ProjTask'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pt_projid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Project']"}),
            'pt_taskid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tasks.Task']"})
        },
        u'tasks.authorisestruct': {
            'Meta': {'object_name': 'AuthoriseStruct'},
            'as_info': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'as_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'as_u1_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'as_u2_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'as_u3_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'as_u4_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'as_user1_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'as_user1_id'", 'to': u"orm['auth.User']"}),
            'as_user1_level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'as_user2_id': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'as_user2_id'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'as_user2_level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'as_user3_id': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'as_user3_id'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'as_user3_level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'as_user4_id': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'as_user4_id'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'as_user4_level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'tasks.task': {
            'Meta': {'object_name': 'Task'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ta_adrid_from': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'Task-From'", 'to': u"orm['contacts.Address']"}),
            'ta_adrid_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'Task-To'", 'to': u"orm['contacts.Address']"}),
            'ta_begin': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'ta_begintime': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'ta_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ta_editor': ('django.db.models.fields.related.ForeignKey', [], {'default': u"orm['auth.User']", 'to': u"orm['auth.User']"}),
            'ta_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'ta_endtime': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'ta_longtxt': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ta_parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'Parent'", 'null': 'True', 'to': u"orm['tasks.Task']"}),
            'ta_priority': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'ta_shorttxt': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'ta_tasktype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tasks.TaskType']"}),
            'ta_warn': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'tasks.tasktype': {
            'Meta': {'object_name': 'TaskType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tt_authstruct_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tasks.AuthoriseStruct']"}),
            'tt_info': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'tt_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tt_template': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['projects']