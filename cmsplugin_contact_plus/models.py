import threading

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from inline_ordering.models import Orderable

try:
    DEFAULT_FROM_EMAIL_ADDRESS = settings.ADMINS[0][1] 
except:
    DEFAULT_FROM_EMAIL_ADDRESS = ''
 
import .utils as utils

 
localdata = threading.local()
localdata.TEMPLATE_CHOICES = utils.autodiscover_templates()
TEMPLATE_CHOICES = localdata.TEMPLATE_CHOICES
    
class ContactPlus(CMSPlugin):
    class Meta:
        verbose_name = "Contact Plus Form"
        verbose_name_plural = "Contact Plus Forms"
    reciepient_email = models.EmailField(_("Email of recipients"), default=DEFAULT_FROM_EMAIL_ADDRESS)
    thanks = models.TextField(_('Message displayed after submitting the contact form.'))
    submit = models.CharField(_('Text for the Submit button.'), blank=True, max_length=30)
    template = models.CharField(max_length=255,
                                choices=TEMPLATE_CHOICES,
                                default='cmsplugin_contact_plus/contact.html',
                                editable=len(TEMPLATE_CHOICES) > 1)
                                   
    def copy_relations(self, oldinstance):
        for extrafield in ExtraField.objects.filter(form__pk=oldinstance.pk):
            extrafield.pk = None
            extrafield.save()
            self.extrafield_set.add(extrafield)
            
    def __unicode__(self):
        return "Contact Plus Form for %s" % self.reciepient_email 


FIELD_TYPE = (('CharField', 'CharField'),
              ('BooleanField', 'BooleanField'),
              ('EmailField','EmailField'),
              ('DecimalField', 'DecimalField'),
              ('FloatField','FloatField'),
              ('IntegerField','IntegerField'),
              ('IPAddressField', 'IPAddressField'),
              #('CharField_Textarea','Textarea'),      
              ('auto_Textarea','CharField as Textarea'),    
              ('auto_hidden_input','CharField as HiddenInput'),    
              ('auto_referral_page','Referral page as HiddenInput'),         
              ('auto_GET_parameter','GET parameter as HiddenInput'),             
)


class ExtraField(Orderable):
    form = models.ForeignKey(ContactPlus, verbose_name=_("Contact Form"))
    label = models.CharField(_('Label'), max_length=100)
    fieldType = models.CharField(max_length=100, choices=FIELD_TYPE)
    initial = models.CharField(_('Inital Value'), max_length=250, blank=True, null=True)
    required = models.BooleanField( _('Mandatory field'), default=True) 
    widget = models.CharField(_('Widget'), max_length=250, blank=True, null=True, help_text="Will be ignored in the current version." )
    
    def __unicode__(self):
        return self.label
