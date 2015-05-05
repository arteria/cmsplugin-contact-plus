from django.contrib import admin
from django.http import HttpResponse

from inline_ordering.admin import OrderableStackedInline
from cmsplugin_contact_plus.models import ExtraField, ContactPlus, ContactRecord

from .actions import export_as_csv_action

class ExtraFieldInline(OrderableStackedInline):
    model = ExtraField


class ContactFormPlusAdmin(admin.ModelAdmin):
    model = ContactPlus
    inlines = (ExtraFieldInline, )


class ContactRecordAdmin(admin.ModelAdmin):
    model = ContactRecord
    actions = [export_as_csv_action("CSV Export", 
        fields = ['contact_form', 'date_of_entry', 'date_processed', 'data'],
        header = True,
        json_fields = ['data']), # 
    ]


admin.site.register(ExtraField)

admin.site.register(ContactRecord, ContactRecordAdmin)
admin.site.register(ContactPlus, ContactFormPlusAdmin)
