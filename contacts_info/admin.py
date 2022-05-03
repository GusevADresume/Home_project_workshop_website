from django.contrib import admin
from contacts_info.models import Contacts_info,Phone


class PhoneInLine(admin.StackedInline):
    model = Phone

@admin.register(Contacts_info)
class ContactsAdmin(admin.ModelAdmin):
    inlines = [PhoneInLine,]