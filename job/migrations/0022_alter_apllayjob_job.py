# Generated by Django 3.2.9 on 2022-02-08 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0021_auto_20220207_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apllayjob',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apply_job', to='job.job'),
        ),
    ]
