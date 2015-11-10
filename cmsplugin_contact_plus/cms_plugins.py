from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cmsplugin_contact_plus.admin import ExtraFieldInline
from cmsplugin_contact_plus.models import ContactPlus
from cmsplugin_contact_plus.forms import ContactFormPlus


import time

def handle_uploaded_file(f, ts):    
    destination = open('%s/%s' % (settings.MEDIA_ROOT, ts + '-' + f.name), 'wb+')

    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    
    
class CMSContactPlusPlugin(CMSPluginBase):
    """ 
    """
    model = ContactPlus
    inlines = [ExtraFieldInline, ]
    name = _('Contact Form')
    render_template = "cmsplugin_contact_plus/contact.html"
    cache = False

    def render(self, context, instance, placeholder):
        request = context['request']

        if instance and instance.template:
            self.render_template = instance.template

        if request.method == "POST" and "contact_plus_form_" + str(instance.id) in request.POST.keys():
            form = ContactFormPlus(contactFormInstance=instance, 
                    request=request, 
                    data=request.POST, 
                    files=request.FILES)
            if form.is_valid():
                ts = str(int(time.time()))

                for fl in request.FILES:
                    for f in request.FILES.getlist(fl):
                        handle_uploaded_file(f, ts)

                form.send(instance.recipient_email, request, ts, instance, form.is_multipart)
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
            form = ContactFormPlus(contactFormInstance=instance, request=request)
            context.update({
                    'contact': instance,
                    'form': form,
            })
        return context


plugin_pool.register_plugin(CMSContactPlusPlugin)
