# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_contact_plus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactplus',
            name='recipient_email',
            field=models.EmailField(default=b'', max_length=254, verbose_name='Email of recipients'),
        ),
    ]
