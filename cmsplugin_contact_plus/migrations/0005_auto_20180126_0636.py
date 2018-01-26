# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cmsplugin_contact_plus.models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_contact_plus', '0004_auto_20170410_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactplus',
            name='recipient_email',
            field=models.EmailField(verbose_name='Email of recipients', max_length=254, default=cmsplugin_contact_plus.models.get_default_from_email_address),
        ),
    ]
