from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models.pluginmodel import CMSPlugin

from django.conf import settings

class Contact(CMSPlugin):
	site_email = models.EmailField(_('Email reciepient'))
	email_label = models.CharField(_('Email sender label'), max_length=100)
	email_required = models.BooleanField(default=True, _('Uncheck if optional'))
	phone_label = models.CharField(_('Phone label'), blank=True, help_text=_("Optional if empty"), max_length=100)
	phone_required = models.BooleanField(default=True, _('Uncheck if optional'))
	subject_label = models.CharField(_('Subject label'), help_text=_("Use as generic field"), max_length=200)
	subject_required = models.BooleanField(default=True, _('Uncheck if optional'))
	content_label = models.CharField(_('Message content label'), max_length=100)
	thanks = models.CharField(_('Message displayed on successful submit'), max_length=200)
	submit = models.CharField(_('Submit button value'), blank=True, max_length=30)

    inclose = models.CharField(max_length=100, choices=getattr(settings, 'AR_GRID_CLASSES', (('', ''),)), default="")
    
    
	def __unicode__(self):
		return self.site_email
