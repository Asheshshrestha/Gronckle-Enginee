# Generated by Django 2.2.2 on 2020-10-07 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0002_auto_20201007_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websitesettingmodel',
            name='captcha_version',
            field=models.CharField(blank=True, choices=[('V2', 'V2'), ('V2 Invisible', 'V2 Invisible'), ('V3', 'V3')], max_length=30, null=True),
        ),
    ]