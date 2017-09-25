# -*- coding: utf-8 -*-
from django.test import TestCase

from cmsplugin_contact_plus.models import ContactPlus, ExtraField


class ModelTestCase(TestCase):
    def setUp(self):
        self.cp = ContactPlus.objects.create()
        self.ef = ExtraField.objects.create(form=self.cp)

    def test_model_create(self):
        assert self.ef
        assert self.cp
