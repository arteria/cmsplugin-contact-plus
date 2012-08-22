from django import forms
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

class ContactForm(forms.Form):
    email 	= forms.EmailField(required=False) 
    phone 	= forms.CharField(required=False)
    subject	= forms.CharField()
    content	= forms.CharField(widget=forms.Textarea())

    def send(self, site_email):
        email_message = EmailMessage(
            self.cleaned_data['subject'],
                render_to_string("email.txt", {
                    'data': self.cleaned_data,
            }),
                    site_email,
                    [site_email],
                    headers = {
                'Reply-To': self.cleaned_data['email']
                },)
        email_message.send(fail_silently=True)

