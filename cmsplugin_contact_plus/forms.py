from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from django import forms
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.models import Site
from django.template.defaultfilters import slugify
from django.conf import settings


class ContactFormPlus(forms.Form):
    
    def __init__(self, contactFormInstance, request, *args, **kwargs):
        super(ContactFormPlus, self).__init__(*args, **kwargs)
        if 'instance' not in kwargs:
            for extraField in contactFormInstance.extrafield_set.all():
                if extraField.fieldType == 'CharField':
                    self.fields[slugify(extraField.label)] = forms.CharField(label=extraField.label, 
                            initial=extraField.initial, 
                            required=extraField.required)
                elif extraField.fieldType == 'BooleanField':
                    self.fields[slugify(extraField.label)] = forms.BooleanField(label=extraField.label, 
                            initial=extraField.initial, 
                            required=extraField.required)
                elif extraField.fieldType == 'EmailField':
                    self.fields[slugify(extraField.label)] = forms.EmailField(label=extraField.label, 
                            initial=extraField.initial, 
                            required=extraField.required)
                elif extraField.fieldType == 'DecimalField':
                    self.fields[slugify(extraField.label)] = forms.DecimalField(label=extraField.label, 
                            initial=extraField.initial, 
                            required=extraField.required)
                elif extraField.fieldType == 'FloatField':
                    self.fields[slugify(extraField.label)] = forms.FloatField(label=extraField.label, 
                            initial=extraField.initial, 
                            required=extraField.required)
                elif extraField.fieldType == 'IntegerField':
                    self.fields[slugify(extraField.label)] = forms.IntegerField(label=extraField.label, 
                            initial=extraField.initial, 
                            required=extraField.required)
                elif extraField.fieldType == 'IPAddressField':
                    self.fields[slugify(extraField.label)] = forms.IPAddressField(label=extraField.label, 
                            initial=extraField.initial, 
                            required=extraField.required)
                elif extraField.fieldType == 'auto_Textarea':
                    self.fields[slugify(extraField.label)] = forms.CharField(label=extraField.label, 
                            initial=extraField.initial,
                            widget=forms.Textarea,   
                            required=extraField.required)
                elif extraField.fieldType == 'auto_hidden_input':
                    self.fields[slugify(extraField.label)] = forms.CharField(label=extraField.label, 
                            initial = extraField.initial,
                            widget=forms.HiddenInput, 
                            required=False)
                elif extraField.fieldType == 'auto_referral_page':
                    lInitial = "No referral available."
                    if request:
                        lInitial = request.META.get('HTTP_REFERER', 'No referral available.')
                    self.fields[slugify(extraField.label)] = forms.CharField(label=extraField.label, 
                            initial = lInitial, #NOTE: This overwrites extraField.initial! 
                            widget=forms.HiddenInput, 
                            required=False) 
                elif extraField.fieldType == 'auto_GET_parameter':
                    lInitial = "Key/value parameter not available."
                    if request:
                        lInitial = request.GET.get(slugify(extraField.label), 'n/a')
                    self.fields[slugify(extraField.label)] = forms.CharField(label=extraField.label, 
                            initial = lInitial, #NOTE: This overwrites extraField.initial! 
                            widget=forms.HiddenInput, 
                            required=False)
                
                
                
    def send(self, reciepient_email, request):
        current_site = Site.objects.get_current()
        email_message = EmailMessage(
            "[" + current_site.domain.upper() + "]",
                render_to_string("cmsplugin_contact_plus/email.txt", {'data': self.cleaned_data,}),
                    from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', None),
                    to = [reciepient_email, ],
                    headers = {
                        #TODO: use settings to define the label. 
                        # 'Reply-To': self.cleaned_data['email']
                    },)
        email_message.send(fail_silently=True)

            