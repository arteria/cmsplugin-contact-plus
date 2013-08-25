from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from inline_ordering.models import Orderable


class ContactPlus(CMSPlugin):
    reciepient_email = models.EmailField(_("Email of reciepients, split by ','"))
    thanks = models.TextField(_('Message displayed on successful submit of the contact form.'))
    submit = models.CharField(_('Submit button value'), blank=True, max_length=30)
   
    def copy_relations(self, oldinstance):
        for extrafield in ExtraField.objects.filter(form__pk=oldinstance.pk):
            extrafield.pk = None
            extrafield.save()
            self.extrafield_set.add(extrafield)

    def __unicode__(self):
        return "Contact Form"

FIELD_TYPE = (('CharField', 'CharField'),
              ('BooleanField', 'BooleanField'),
              ('EmailField','EmailField'),
              ('DecimalField', 'DecimalField'),
              ('FloatField','FloatField'),
              ('IntegerField','IntegerField'),
              ('IPAddressField', 'IPAddressField'),
              
)
class ExtraField(Orderable):
    form = models.ForeignKey(ContactPlus, verbose_name=_("Contact Form"))
    label = models.CharField(_('Label'), max_length=100)
    fieldType = models.CharField(max_length=100, choices=FIELD_TYPE)
    initial = models.CharField(_('Inital Value'), max_length=250, blank=True, null=True)
    required = models.BooleanField( _('Mandatory field'), default=True) 
    widget = models.CharField(_('Widget'), max_length=250, blank=True, null=True)
    
    def __unicode__(self):
        return self.label
