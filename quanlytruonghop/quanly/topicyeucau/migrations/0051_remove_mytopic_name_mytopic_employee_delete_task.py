# Generated by Django 4.2 on 2023-05-04 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('topicyeucau', '0050_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mytopic',
            name='name',
        ),
        migrations.AddField(
            model_name='mytopic',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
