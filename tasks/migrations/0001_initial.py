# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AuthoriseStruct'
        db.create_table(u'tasks_authorisestruct', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('as_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('as_info', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('as_user1_id', self.gf('django.db.models.fields.related.ForeignKey')(related_name='as_user1_id', to=orm['auth.User'])),
            ('as_user1_level', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('as_u1_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('as_user2_id', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='as_user2_id', null=True, to=orm['auth.User'])),
            ('as_user2_level', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('as_u2_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('as_user3_id', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='as_user3_id', null=True, to=orm['auth.User'])),
            ('as_user3_level', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('as_u3_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('as_user4_id', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='as_user4_id', null=True, to=orm['auth.User'])),
            ('as_user4_level', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('as_u4_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'tasks', ['AuthoriseStruct'])

        # Adding model 'TaskType'
        db.create_table(u'tasks_tasktype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tt_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('tt_info', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('tt_authstruct_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tasks.AuthoriseStruct'])),
            ('tt_template', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'tasks', ['TaskType'])

        # Adding model 'Task'
        db.create_table(u'tasks_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ta_shorttxt', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('ta_longtxt', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('ta_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('ta_editor', self.gf('django.db.models.fields.related.ForeignKey')(default=orm['auth.User'], to=orm['auth.User'])),
            ('ta_begin', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('ta_begintime', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('ta_end', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('ta_endtime', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('ta_warn', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('ta_priority', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('ta_adrid_from', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'Task-From', to=orm['contacts.Address'])),
            ('ta_adrid_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'Task-To', to=orm['contacts.Address'])),
            ('ta_tasktype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tasks.TaskType'])),
            ('ta_parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'Parent', null=True, to=orm['tasks.Task'])),
        ))
        db.send_create_signal(u'tasks', ['Task'])

        # Adding model 'TaskDoc'
        db.create_table(u'tasks_taskdoc', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('td_taksid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tasks.Task'])),
            ('td_docid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['docs.Doc'])),
            ('td_info', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'tasks', ['TaskDoc'])

        # Adding model 'TaskTemplateFields'
        db.create_table(u'tasks_tasktemplatefields', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ttf_company', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'Firma', to=orm['contacts.ContactType'])),
            ('ttf_name', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'Name', to=orm['contacts.ContactType'])),
            ('ttf_form_of_adr', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'Anrede', to=orm['contacts.ContactType'])),
            ('ttf_zipcode', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'PLZ', to=orm['contacts.ContactType'])),
            ('ttf_city', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'Stadt', to=orm['contacts.ContactType'])),
            ('ttf_postboxzip', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'PLZ_Postbox', to=orm['contacts.ContactType'])),
            ('ttf_country', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'Land', to=orm['contacts.ContactType'])),
            ('ttf_fax', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'Fax', to=orm['contacts.ContactType'])),
        ))
        db.send_create_signal(u'tasks', ['TaskTemplateFields'])


    def backwards(self, orm):
        # Deleting model 'AuthoriseStruct'
        db.delete_table(u'tasks_authorisestruct')

        # Deleting model 'TaskType'
        db.delete_table(u'tasks_tasktype')

        # Deleting model 'Task'
        db.delete_table(u'tasks_task')

        # Deleting model 'TaskDoc'
        db.delete_table(u'tasks_taskdoc')

        # Deleting model 'TaskTemplateFields'
        db.delete_table(u'tasks_tasktemplatefields')


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
        u'contacts.category': {
            'Meta': {'object_name': 'Category'},
            'ca_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ca_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'contacts.contacttype': {
            'Meta': {'object_name': 'ContactType'},
            'ct_category_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Category']"}),
            'ct_info': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'ct_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'ct_sort_id': ('django.db.models.fields.IntegerField', [], {}),
            'ct_viewshown': ('django.db.models.fields.BooleanField', [], {}),
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
        u'tasks.taskdoc': {
            'Meta': {'object_name': 'TaskDoc'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'td_docid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['docs.Doc']"}),
            'td_info': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'td_taksid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tasks.Task']"})
        },
        u'tasks.tasktemplatefields': {
            'Meta': {'object_name': 'TaskTemplateFields'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ttf_city': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'Stadt'", 'to': u"orm['contacts.ContactType']"}),
            'ttf_company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'Firma'", 'to': u"orm['contacts.ContactType']"}),
            'ttf_country': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'Land'", 'to': u"orm['contacts.ContactType']"}),
            'ttf_fax': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'Fax'", 'to': u"orm['contacts.ContactType']"}),
            'ttf_form_of_adr': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'Anrede'", 'to': u"orm['contacts.ContactType']"}),
            'ttf_name': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'Name'", 'to': u"orm['contacts.ContactType']"}),
            'ttf_postboxzip': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'PLZ_Postbox'", 'to': u"orm['contacts.ContactType']"}),
            'ttf_zipcode': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'PLZ'", 'to': u"orm['contacts.ContactType']"})
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

    complete_apps = ['tasks']