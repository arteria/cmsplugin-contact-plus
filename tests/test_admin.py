# -*- coding: utf-8 -*-
from django.test import TestCase
from django.contrib.admin.sites import AdminSite

from cmsplugin_contact_plus import admin
from cmsplugin_contact_plus import models


class AdminTestCase(TestCase):
    def test_contact_form_plus_admin(self):
        test_admin = admin.ContactFormPlusAdmin(models.ContactPlus, AdminSite())
        assert test_admin
        assert test_admin.model
        assert test_admin.admin_site

    def test_contact_record_admin(self):
        test_admin = admin.ContactRecordAdmin(models.ContactRecord, AdminSite())
        assert test_admin
        assert test_admin.model
        assert test_admin.admin_site
