# Generated by Django 4.1.7 on 2023-04-11 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topicyeucau', '0023_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(default='5555555555', max_length=15),
        ),
    ]
