# Generated by Django 4.2.5 on 2023-09-08 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('send_sms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smssettings',
            name='Static Parameters',
        ),
        migrations.CreateModel(
            name='SMSParameters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Parameter', models.CharField(max_length=128)),
                ('value', models.CharField(max_length=128)),
                ('header', models.BooleanField(default=False)),
                ('sms_settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='send_sms.smssettings')),
            ],
        ),
    ]