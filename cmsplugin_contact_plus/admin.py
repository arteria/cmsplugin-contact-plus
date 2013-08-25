from django.contrib import admin

from inline_ordering.admin import OrderableStackedInline

from .models import ExtraField, ContactPlus


class ExtraFieldInline(OrderableStackedInline):
    model = ExtraField


class ContactFormPlusAdmin(admin.ModelAdmin):
    model = ContactPlus
    inlines = (ExtraFieldInline, )


admin.site.register(ExtraField)
admin.site.register(ContactPlus, ContactFormPlusAdmin)

