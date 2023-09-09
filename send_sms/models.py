from django.db import models

# Create your models here.


class SMSSettings(models.Model):
    sms_gateway_url = models.URLField(
        blank=False, help_text='Eg. smsgateway.com/api/send_sms.cgi')
    message_parameter = models.CharField(
        blank=False, help_text='Enter url parameter for message', max_length=64)
    receiver_parameter = models.CharField(
        blank=False, help_text='Enter url parameter for receiver nos', max_length=64)
    use_post = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'SMS Settings'

    def __str__(self) -> str:
        return 'SMS Settings'


class SMSParameters(models.Model):
    parameter = models.CharField(max_length=128, blank=False)
    value = models.CharField(max_length=128, blank=False)
    header = models.BooleanField(default=False)
    sms_settings = models.ForeignKey(SMSSettings, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.parameter

class SMS_Log(models.Model):
    sent_on = models.DateTimeField(auto_now=True)
    message = models.TextField()
    sent_to = models.CharField(max_length=28)

    class Meta:
        verbose_name_plural = 'SMS Logs'
