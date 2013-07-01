from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models.pluginmodel import CMSPlugin

from django.conf import settings

class Contact(CMSPlugin):
    site_email = models.EmailField(_("Email reciepients, split by ','"))
    
    email_label = models.CharField(_('Email sender label'), max_length=100)
    email_required = models.BooleanField( _('Mandatory field'), default=True)
    
    phone_label = models.CharField(_('Phone label'), blank=True, help_text=_("Field will not be rendered if left empty"), max_length=100)
    phone_required = models.BooleanField( _('Mandatory field'), default=True)
    
    subject_label = models.CharField(_('Subject label'), help_text=_("Use as generic field"), max_length=200)
    subject_required = models.BooleanField( _('Mandatory field'), default=True)
    
    content_label = models.CharField(_('Message content label'), max_length=100)
    thanks = models.TextField(_('Message displayed on successful submit'))
    
    
    submit = models.CharField(_('Submit button value'), blank=True, max_length=30)
    inclose = models.CharField(max_length=100, choices=getattr(settings, 'AR_GRID_CLASSES', (('', ''),)), default="")
        
#    status = new/read/
    
    
    def __unicode__(self):
        return self.site_email
