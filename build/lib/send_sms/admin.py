from django.contrib import admin
from django.http.request import HttpRequest

from send_sms.models import SMS_Log, SMSParameters, SMSSettings

# Register your models here.


class SMSParametersAdmin(admin.TabularInline):
    model = SMSParameters


class SMSSettingsAdmin(admin.ModelAdmin):
    inlines = [SMSParametersAdmin]

    def has_add_permission(self, request: HttpRequest) -> bool:
        return not SMSSettings.objects.exists()


@admin.register(SMS_Log)
class SMSLogAdmin(admin.ModelAdmin):
    list_display = ['sent_to', 'sent_on', 'message']
    readonly_fields = ['sent_to', 'sent_on', 'message']


admin.site.register(SMSSettings, SMSSettingsAdmin)
