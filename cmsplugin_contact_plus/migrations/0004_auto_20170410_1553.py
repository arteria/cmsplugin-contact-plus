# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_contact_plus', '0003_auto_20161102_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='extrafield',
            name='placeholder',
            field=models.CharField(max_length=250, null=True, verbose_name='Placeholder Value', blank=True),
        ),
        migrations.AlterField(
            model_name='contactplus',
            name='recipient_email',
            field=models.EmailField(default=b'', max_length=254, verbose_name='Email of recipients'),
        ),
    ]
