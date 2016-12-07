from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import importlib


def send_email(**kwargs):
    sender = getattr(settings, 'CONTACT_PLUS_SEND_METHOD', None)
    if sender:
        met, func = sender.rsplit('.', 1)
        sender = getattr(importlib.import_module(met), func)

        return sender(**kwargs)
    return default_send_email(**kwargs)


def default_send_email(**kwargs):
    email_message = EmailMessage(
        subject=kwargs['subject'],
        body=render_to_string(
            "cmsplugin_contact_plus/email.txt", kwargs['context']),
        from_email=kwargs['from_email'],
        to=kwargs['to'],
        headers=kwargs['headers'],
    )
    email_message.send(fail_silently=True)


def none_send_email(**kwargs):
    pass
