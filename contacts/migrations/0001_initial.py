# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Address'
        db.create_table(u'contacts_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('adr_searchname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('adr_email', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'contacts', ['Address'])

        # Adding model 'Category'
        db.create_table(u'contacts_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ca_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ca_description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'contacts', ['Category'])

        # Adding model 'ContactType'
        db.create_table(u'contacts_contacttype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ct_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('ct_info', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('ct_category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Category'])),
            ('ct_sort_id', self.gf('django.db.models.fields.IntegerField')()),
            ('ct_viewshown', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'contacts', ['ContactType'])

        # Adding model 'ContactData'
        db.create_table(u'contacts_contactdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cd_contacttype_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.ContactType'])),
            ('cd_textfield', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cd_address_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Address'])),
        ))
        db.send_create_signal(u'contacts', ['ContactData'])

        # Adding model 'ContactDataFulltext'
        db.create_table(u'contacts_contactdatafulltext', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cf_contacttype_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.ContactType'])),
            ('cf_textfield', self.gf('django.db.models.fields.TextField')()),
            ('cf_address_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Address'])),
        ))
        db.send_create_signal(u'contacts', ['ContactDataFulltext'])


    def backwards(self, orm):
        # Deleting model 'Address'
        db.delete_table(u'contacts_address')

        # Deleting model 'Category'
        db.delete_table(u'contacts_category')

        # Deleting model 'ContactType'
        db.delete_table(u'contacts_contacttype')

        # Deleting model 'ContactData'
        db.delete_table(u'contacts_contactdata')

        # Deleting model 'ContactDataFulltext'
        db.delete_table(u'contacts_contactdatafulltext')


    models = {
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
        u'contacts.contactdata': {
            'Meta': {'object_name': 'ContactData'},
            'cd_address_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Address']"}),
            'cd_contacttype_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.ContactType']"}),
            'cd_textfield': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'contacts.contactdatafulltext': {
            'Meta': {'object_name': 'ContactDataFulltext'},
            'cf_address_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Address']"}),
            'cf_contacttype_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.ContactType']"}),
            'cf_textfield': ('django.db.models.fields.TextField', [], {}),
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
        }
    }

    complete_apps = ['contacts']