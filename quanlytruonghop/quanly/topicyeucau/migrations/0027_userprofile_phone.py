# Generated by Django 4.1.7 on 2023-04-11 07:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topicyeucau', '0026_remove_userprofile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator(message='Số điện thoại phải có 10 chữ số.', regex='^\\d{10}$')]),
        ),
    ]
