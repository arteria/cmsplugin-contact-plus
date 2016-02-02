from django import forms
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.models import Site
from django.template.defaultfilters import slugify
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from captcha.fields import ReCaptchaField
from simplemathcaptcha.fields import MathCaptchaField
from cmsplugin_contact_plus.models import ContactPlus, ContactRecord
from cmsplugin_contact_plus.signals import contact_message_sent
from cmsplugin_contact_plus.utils import get_validators

class ContactFormPlus(forms.Form):
    required_css_class = getattr(settings, 'CONTACT_PLUS_REQUIRED_CSS_CLASS', 'required')

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
                elif extraField.fieldType == 'FileField': 
                    self.fields[slugify(extraField.label)] = forms.FileField(label=extraField.label,
                            initial=extraField.initial,
                            required=extraField.required)
                elif extraField.fieldType == 'ImageField': 
                    self.fields[slugify(extraField.label)] = forms.ImageField(label=extraField.label,
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
                            initial=extraField.initial,
                            widget=forms.HiddenInput,
                            required=False)
                elif extraField.fieldType == 'auto_referral_page':
                    lInitial = _("No referral available.")
                    if request:
                        lInitial = request.META.get('HTTP_REFERER', _('No referral available.'))
                    self.fields[slugify(extraField.label)] = forms.CharField(label=extraField.label,
                            initial=lInitial,  # NOTE: This overwrites extraField.initial!
                            widget=forms.HiddenInput,
                            required=False)
                elif extraField.fieldType == 'MathCaptcha':
                    self.fields[slugify(extraField.label)] = MathCaptchaField(
                                                label=extraField.label,
                                                initial=extraField.initial,
                                                required=True)
                elif extraField.fieldType == 'ReCaptcha':
                    self.fields[slugify(extraField.label)] = ReCaptchaField(
                                                label=extraField.label,
                                                initial=extraField.initial,
                                                required=True)
                elif extraField.fieldType == 'auto_GET_parameter':
                    lInitial = _("Key/value parameter not available.")
                    if request:
                        lInitial = request.GET.get(slugify(extraField.label), 'n/a')
                    self.fields[slugify(extraField.label)] = forms.CharField(label=extraField.label,
                            initial=lInitial,  # NOTE: This overwrites extraField.initial!
                            widget=forms.HiddenInput,
                            required=False)
                elif extraField.fieldType == 'CharFieldWithValidator':
                    self.fields[slugify(extraField.label)] = forms.CharField(
                        label=extraField.label,
                        initial=extraField.initial,
                        required=extraField.required,
                        validators=get_validators())


    def send(self, recipient_email, request, ts, instance=None, multipart=False):
        current_site = Site.objects.get_current()
        if instance:
            order = ContactPlus.objects.get(id=instance.id).extrafield_set.order_by('inline_ordering_position')
            excluded_field_types = ['MathCaptcha', 'ReCaptcha']
            order = [field for field in order if field.fieldType not in excluded_field_types]
            ordered_dic_list = []
            for field in order:
                key = slugify(field.label)
                value = self.cleaned_data.get(key, '(no input)')
                # redefine value for files... 
                if field.fieldType in ["FileField", "ImageField"]:
                    val = ts + '-' + str(value)
                    if settings.MEDIA_URL.startswith("http"):
                        value = "%s%s" % (settings.MEDIA_URL, val)
                    else:
                        value = "http://%s%s%s" % (current_site, settings.MEDIA_URL, val)
                ordered_dic_list.append({field.label: value})

        # Automatically match reply-to email address in form
        tmp_headers = {}
        try:
            reply_email_label = getattr(settings, 'CONTACT_PLUS_REPLY_EMAIL_LABEL', None)
            if reply_email_label is not None:
                tmp_headers.update({'Reply-To': self.cleaned_data[reply_email_label]})
        except:
            pass

        email_message = EmailMessage(
            subject=instance.email_subject,
            body=render_to_string("cmsplugin_contact_plus/email.txt", {'data': self.cleaned_data,
                                                                      'ordered_data': ordered_dic_list,
                                                                      'instance': instance,
                                                                      }),
            from_email=getattr(settings, 'CONTACT_PLUS_FROM_EMAIL', settings.DEFAULT_FROM_EMAIL),
            to=[recipient_email, ],
            headers=tmp_headers,
        )
        email_message.send(fail_silently=True)

        if instance.collect_records:# and not multipart:
            record = ContactRecord(contact_form=instance, data=ordered_dic_list)#self.cleaned_data)
            record.save()

        contact_message_sent.send(sender=self, data=self.cleaned_data)
