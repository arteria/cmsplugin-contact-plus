# -*- coding: utf-8 -*-
from django.core.checks import Warning, register


def warn_1_3_changes(app_configs, **kwargs):
    return [
        Warning(
            'cmsplugin-contact-plus >= 1.3 has renamed the "input" field. Do not forget to migrate your '
            'database and update your templates',
            hint=None,
            obj=None,
            id='cmsplugin_contact_plus.W001',
        )
    ]


def register_checks():
    for check in [
        warn_1_3_changes,
    ]:
        register(check)
