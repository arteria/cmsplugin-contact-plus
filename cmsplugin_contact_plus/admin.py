from django.contrib import admin
from django.http import HttpResponse

from adminsortable.admin import SortableTabularInline, NonSortableParentAdmin
from cmsplugin_contact_plus.models import ExtraField, ContactPlus, ContactRecord

from .actions import export_as_csv_action

class ExtraFieldInline(SortableTabularInline):
    model = ExtraField
    fields = ('label', 'fieldType', 'initial', 'placeholder', 'required')


class ContactFormPlusAdmin(NonSortableParentAdmin):
    model = ContactPlus
    inlines = (ExtraFieldInline, )


class ContactRecordAdmin(admin.ModelAdmin):
    model = ContactRecord
    list_display = ('contact_form', 'date_of_entry')
    ordering = ['-date_of_entry']
    search_fields = ['contact_form']    
    actions = [export_as_csv_action("CSV Export", 
        fields = ['contact_form', 'date_of_entry', 'date_processed', 'data'],
        header = True,
        json_fields = ['data']), # 
    ]


admin.site.register(ExtraField)

admin.site.register(ContactRecord, ContactRecordAdmin)
admin.site.register(ContactPlus, ContactFormPlusAdmin)
