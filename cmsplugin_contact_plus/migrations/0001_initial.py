# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import cmsplugin_contact_plus.models
import jsonfield.fields

from cmsplugin_contact_plus.models import FIELD_TYPE


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPlus',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(help_text='Title for the Contact Form.', max_length=100, null=True, verbose_name='Title', blank=True)),
                ('email_subject', models.CharField(default=cmsplugin_contact_plus.models.get_current_site, max_length=256, verbose_name='Email subject')),
                ('recipient_email', models.EmailField(default=b'', max_length=75, verbose_name='Email of recipients')),
                ('collect_records', models.BooleanField(default=True, help_text='If active, all records for this Form will be stored in the Database.', verbose_name='Collect Records')),
                ('thanks', models.TextField(verbose_name='Message displayed after submitting the contact form.')),
                ('submit', models.CharField(max_length=30, verbose_name='Text for the Submit button.', blank=True)),
                ('template', models.CharField(default=b'cmsplugin_contact_plus/contact.html', max_length=255, editable=False, choices=[(b'cmsplugin_contact_plus/contact.html', b'contact.html')])),
            ],
            options={
                'verbose_name': 'Contact Plus Form',
                'verbose_name_plural': 'Contact Plus Forms',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='ContactRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_entry', models.DateTimeField(auto_now_add=True)),
                ('date_processed', models.DateTimeField(help_text=b'Date the Record was processed.', null=True, blank=True)),
                ('data', jsonfield.fields.JSONField(default={}, null=True, blank=True)),
                ('contact_form', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='Contact Form', to='cmsplugin_contact_plus.ContactPlus', null=True)),
            ],
            options={
                'ordering': ['date_of_entry', 'contact_form'],
                'verbose_name': 'Contact Record',
                'verbose_name_plural': 'Contact Records',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExtraField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inline_ordering_position', models.IntegerField(null=True, blank=True)),
                ('label', models.CharField(max_length=100, verbose_name='Label')),
                ('fieldType', models.CharField(max_length=100, choices=FIELD_TYPE)),
                ('initial', models.CharField(max_length=250, null=True, verbose_name='Inital Value', blank=True)),
                ('required', models.BooleanField(default=True, verbose_name='Mandatory field')),
                ('widget', models.CharField(help_text='Will be ignored in the current version.', max_length=250, null=True, verbose_name='Widget', blank=True)),
                ('form', models.ForeignKey(verbose_name='Contact Form', to='cmsplugin_contact_plus.ContactPlus')),
            ],
            options={
                'ordering': ('inline_ordering_position',),
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
