from django.utils.translation import ugettext_lazy as _
from django.forms.formsets import BaseFormSet

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .admin import ExtraFieldInline
from .models import ContactPlus
from .forms import ContactFormPlus


class CMSContactPlusPlugin(CMSPluginBase):
    model = ContactPlus
    inlines = [ExtraFieldInline, ]
    name = _('Contact Form')
    render_template = "cmsplugin_contact_plus/contact.html"

    def render(self, context, instance, placeholder):
        request = context['request']
        if request.method == "POST":
            form = ContactFormPlus(contactFormInstance=instance, data=request.POST)
            if form.is_valid():
                form.send(instance.reciepient_email, request)
                context.update({
                    'contact': instance,
                })
                return context
            else:
                context.update({
                    'contact': instance,
                    'form': form,
                        
                })
        else:
            kw = {'request': request, }
            form = ContactFormPlus(contactFormInstance=instance, **kw) 
            context.update({
                    'contact': instance,
                    'form': form,
            })
        return context


plugin_pool.register_plugin(CMSContactPlusPlugin)
