# Generated by Django 4.2.5 on 2023-09-08 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('send_sms', '0002_remove_smssettings_static_parameters_smsparameters'),
    ]

    operations = [
        migrations.RenameField(
            model_name='smsparameters',
            old_name='Parameter',
            new_name='parameter',
        ),
        migrations.RenameField(
            model_name='smssettings',
            old_name='SMS Gateway URL',
            new_name='sms_gateway_url',
        ),
        migrations.RenameField(
            model_name='smssettings',
            old_name='Use POST',
            new_name='use_post',
        ),
    ]