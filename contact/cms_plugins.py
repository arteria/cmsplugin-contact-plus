from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from plugins.contact.models import Contact
from plugins.contact.forms import ContactForm

class ContactPlugin(CMSPluginBase):
    model = Contact
    name = _("Contact Form")
    render_template = "contact.html"
    
    def render(self, context, instance, placeholder):
	request = context['request']

	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			form.send(instance.site_email)
			context.update( {
				'contact': instance,
				})
			return context
	else:
		form = ContactForm()

	
        context.update({
		'contact': instance,
		'form': form,
        	})
        return context
    
plugin_pool.register_plugin(ContactPlugin)
