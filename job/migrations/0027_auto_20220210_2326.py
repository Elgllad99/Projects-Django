# Generated by Django 3.2.9 on 2022-02-10 21:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0026_alter_apllayjob_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='apllayjob',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='apllayjob',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
