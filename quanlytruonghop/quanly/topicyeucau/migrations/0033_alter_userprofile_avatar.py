# Generated by Django 4.2 on 2023-04-18 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topicyeucau', '0032_alter_userprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='avatar/man.png', upload_to='avatars/'),
        ),
    ]
