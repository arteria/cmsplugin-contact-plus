from django.contrib import admin

from inline_ordering.admin import OrderableStackedInline
from cmsplugin_contact_plus.models import ExtraField, ContactPlus, ContactRecord


class ExtraFieldInline(OrderableStackedInline):
    model = ExtraField


class ContactFormPlusAdmin(admin.ModelAdmin):
    model = ContactPlus
    inlines = (ExtraFieldInline, )


admin.site.register(ExtraField)
admin.site.register(ContactRecord)
admin.site.register(ContactPlus, ContactFormPlusAdmin)
