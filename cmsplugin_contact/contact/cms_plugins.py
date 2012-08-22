from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import Contact
from forms import ContactForm

class ContactPlugin(CMSPluginBase):
    model = Contact
    name = _("Contact Form")
    render_template = "contact.html"
     
    def render(self, context, instance, placeholder):
        request = context['request']
        if request.method == "POST":
            form = ContactForm(request.POST)
            
            form.fields['email'].required = instance.email_required
            form.fields['phone'].required = instance.phone_required
            form.fields['subject'].required = instance.subject_required
                
            if form.is_valid():
                form.send(instance.site_email)
                context.update({
                        'contact': instance,
                        })
                return context
            else:
            #    form = ContactForm()
            #    form.fields['email'].required = instance.email_required
            #    form.fields['phone'].required = instance.phone_required
            #    form.fields['subject'].required = instance.subject_required
                
                context.update({
                'contact': instance,
                'form': form,
                'hasError': True,
                 })
        
         
        else:
            # GET
            form = ContactForm()
            form.fields['email'].required = instance.email_required
            form.fields['phone'].required = instance.phone_required
            form.fields['subject'].required = instance.subject_required
            
            context.update({
            'contact': instance,
            'form': form,
                })
        return context

         
plugin_pool.register_plugin(ContactPlugin)
