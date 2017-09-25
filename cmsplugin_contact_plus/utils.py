# -*- coding: utf-8 -*-
import importlib

from django.conf import settings


def get_validators():
    val = []
    # See if validators have been defined
    if hasattr(settings, 'CMSPLUGIN_CONTACT_FORM_VALIDATORS'):
        validators = getattr(settings,
                             'CMSPLUGIN_CONTACT_FORM_VALIDATORS')
        for validator in validators:
            try:
                f = getattr(importlib.import_module(validator[0]),
                            validator[1])
                val.append(f)
            except ImportError:
                raise ImportError(
                    "Cannot import {} from module {}.".format(
                        validator[1], validator[0]))
    return val
