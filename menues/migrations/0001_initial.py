# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Image'
        db.create_table(u'menues_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image_subject', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('image_file', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'menues', ['Image'])

        # Adding model 'Menu'
        db.create_table(u'menues_menu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('linkintern', self.gf('django.db.models.fields.BooleanField')()),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'Parent', null=True, to=orm['menues.Menu'])),
            ('menu_hide', self.gf('django.db.models.fields.BooleanField')()),
            ('date_creation', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_last_edit', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'menues', ['Menu'])

        # Adding model 'MetaInfos'
        db.create_table(u'menues_metainfos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('metainfo_subject', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('metainfo', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'menues', ['MetaInfos'])


    def backwards(self, orm):
        # Deleting model 'Image'
        db.delete_table(u'menues_image')

        # Deleting model 'Menu'
        db.delete_table(u'menues_menu')

        # Deleting model 'MetaInfos'
        db.delete_table(u'menues_metainfos')


    models = {
        u'menues.image': {
            'Meta': {'object_name': 'Image'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image_subject': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'menues.menu': {
            'Meta': {'ordering': "['-date_creation']", 'object_name': 'Menu'},
            'date_creation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_last_edit': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'linkintern': ('django.db.models.fields.BooleanField', [], {}),
            'menu_hide': ('django.db.models.fields.BooleanField', [], {}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'Parent'", 'null': 'True', 'to': u"orm['menues.Menu']"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'menues.metainfos': {
            'Meta': {'object_name': 'MetaInfos'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metainfo': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'metainfo_subject': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['menues']