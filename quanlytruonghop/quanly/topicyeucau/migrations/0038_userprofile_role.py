# Generated by Django 4.2 on 2023-05-03 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topicyeucau', '0037_userprofile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(default='Sinh viên', max_length=255),
        ),
    ]
