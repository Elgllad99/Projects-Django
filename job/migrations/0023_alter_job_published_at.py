# Generated by Django 3.2.9 on 2022-02-08 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0022_alter_apllayjob_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='published_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
