# Generated by Django 3.2.9 on 2022-01-26 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20220125_2100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='companyName',
        ),
    ]
