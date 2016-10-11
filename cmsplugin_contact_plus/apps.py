# -*- coding: utf-8 -*-
from django.apps import AppConfig


class ContactPlusConfig(AppConfig):
    name = 'cmsplugin_contact_plus'
    verbose_name = 'CMSPlugin Contact Plus'

    def ready(self):
        from cmsplugin_contact_plus.checks import register_checks
        register_checks()
