# Generated by Django 3.2.9 on 2021-12-28 12:51

from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0015_alter_job_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='img',
            field=models.ImageField(height_field='height', max_length=82, upload_to=job.models.image_upload, width_field='width'),
        ),
    ]
