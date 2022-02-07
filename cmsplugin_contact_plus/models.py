from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site
from django.utils.encoding import python_2_unicode_compatible
from django.db.models import Model

from cms.models import CMSPlugin
from adminsortable.models import SortableMixin
from jsonfield import JSONField

from cmsplugin_contact_plus import local_settings


def get_default_from_email_address():
    email_address = ''
    try:
        email_address = settings.ADMINS[0][1]
    except:
        pass

    return email_address


def get_current_site():
    try:
        current_site = Site.objects.get_current()
    except:
        current_site = 'example.com'
    return _('Contact form message from {}').format(current_site)


@python_2_unicode_compatible
class ContactPlus(CMSPlugin):
    title = models.CharField(_('Title'),
            null=True,
            blank=True,
            max_length=100,
            help_text=_("Title for the Contact Form."))
    email_subject = models.CharField(
            max_length=256,
            verbose_name=_("Email subject"),
            default=get_current_site)
    recipient_email = models.EmailField(_("Email of recipients"),
            default=get_default_from_email_address,
            max_length=254)
    collect_records = models.BooleanField(_('Collect Records'),
            default=True,
            help_text=_("If active, all records for this Form will be stored in the Database."))
    thanks = models.TextField(_('Message displayed after submitting the contact form.'))
    submit_button_text = models.CharField(_('Text for the Submit button.'),
            blank=True,
            max_length=30)
    template = models.CharField(
            max_length=255,
            choices=local_settings.CMSPLUGIN_CONTACT_PLUS_TEMPLATES,
            default='cmsplugin_contact_plus/contact.html',
            editable=len(local_settings.CMSPLUGIN_CONTACT_PLUS_TEMPLATES) > 1)

    class Meta:
        verbose_name = "Contact Plus Form"
        verbose_name_plural = "Contact Plus Forms"

    def copy_relations(self, oldinstance):
        for extrafield in ExtraField.objects.filter(form__pk=oldinstance.pk):
            extrafield.pk = None
            extrafield.save()
            self.extrafield_set.add(
                extrafield)

    def __str__(self):
        if self.title:
            return self.title
        return _("Contact Plus Form for %s") % self.recipient_email


def recaptcha_installed():
    return ('captcha' in settings.INSTALLED_APPS and
            all([hasattr(settings, s)
                for s in ['RECAPTCHA_PUBLIC_KEY', 'RECAPTCHA_PRIVATE_KEY']]))

FIELD_TYPE = (('CharField', 'CharField'),
              ('BooleanField', 'BooleanField'),
              ('EmailField', 'EmailField'),
              ('DecimalField', 'DecimalField'),
              ('FloatField', 'FloatField'),
              ('IntegerField', 'IntegerField'),
              ('DateField', 'DateField'),
              ('DateTimeField', 'DateTimeField'),
              ('FileField', 'FileField'),
              ('ImageField', 'ImageField'),
              ('IPAddressField', 'IPAddressField'),
              ('MathCaptcha', 'Math Captcha'),
              ('auto_Textarea', _('CharField as Textarea')),
              ('auto_hidden_input', _('CharField as HiddenInput')),
              ('auto_referral_page', _('Referral page as HiddenInput')),
              ('auto_GET_parameter', _('GET parameter as HiddenInput')),
              ('CharFieldWithValidator', 'CharFieldWithValidator'),)
if recaptcha_installed():
    FIELD_TYPE += (('ReCaptcha', 'reCAPTCHA'),)


@python_2_unicode_compatible
class ExtraField(SortableMixin):
    """
    """
    form = models.ForeignKey(ContactPlus, verbose_name=_("Contact Form"), null=True, on_delete=models.SET_NULL)
    label = models.CharField(_('Label'), max_length=100)
    fieldType = models.CharField(max_length=100, choices=FIELD_TYPE)
    initial = models.CharField(
        _('Inital Value'), max_length=250, blank=True, null=True)
    placeholder = models.CharField(
        _('Placeholder Value'), max_length=250, blank=True, null=True)
    required = models.BooleanField(
        _('Mandatory field'), default=True)
    widget = models.CharField(
        _('Widget'), max_length=250, blank=True, null=True,
        help_text=_("Will be ignored in the current version."))

    inline_ordering_position = models.IntegerField(blank=True, null=True, editable=True)

    def __str__(self):
        return self.label

    class Meta:
        ordering = ('inline_ordering_position',)


@python_2_unicode_compatible
class ContactRecord(Model):
    """
    """
    contact_form = models.ForeignKey(ContactPlus, verbose_name=_("Contact Form"), null=True, on_delete=models.SET_NULL)
    date_of_entry = models.DateTimeField(auto_now_add=True)
    date_processed = models.DateTimeField(null=True, blank=True, help_text=_("Date the Record was processed."))
    data = JSONField(null=True, blank=True, default={})

    class Meta():
        ordering = ['date_of_entry', 'contact_form', ]
        verbose_name = _("Contact Record")
        verbose_name_plural = _("Contact Records")

    @property
    def is_processed(self):
        if self.date_processed:
            return True
        else:
            return False

    def __str__(self):
        return _(u"Record for %(contact)s recorded on %(date)s") % {'contact':self.contact_form,
                                                                   'date': self.date_of_entry.strftime('%d. %b %Y') }
