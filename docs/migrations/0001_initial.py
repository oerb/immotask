# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DocType'
        db.create_table(u'docs_doctype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dt_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('dt_info', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'docs', ['DocType'])

        # Adding model 'Doc'
        db.create_table(u'docs_doc', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('doc_subject', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('doc_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'docs', ['Doc'])


    def backwards(self, orm):
        # Deleting model 'DocType'
        db.delete_table(u'docs_doctype')

        # Deleting model 'Doc'
        db.delete_table(u'docs_doc')


    models = {
        u'docs.doc': {
            'Meta': {'object_name': 'Doc'},
            'doc_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'doc_subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'docs.doctype': {
            'Meta': {'object_name': 'DocType'},
            'dt_info': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'dt_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['docs']