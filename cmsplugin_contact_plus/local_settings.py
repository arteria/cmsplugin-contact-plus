from django.conf import settings

CMSPLUGIN_CONTACT_PLUS_TEMPLATES = getattr(settings, 'CMSPLUGIN_CONTACT_PLUS_TEMPLATES', [
    ('cmsplugin_contact_plus/contact.html', 'contact.html'),
])
