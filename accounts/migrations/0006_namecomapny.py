# Generated by Django 3.2.9 on 2022-01-26 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_profile_company_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='NameComapny',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameComp', models.CharField(max_length=60)),
            ],
        ),
    ]
