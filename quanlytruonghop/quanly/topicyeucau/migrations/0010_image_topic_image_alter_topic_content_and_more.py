# Generated by Django 4.1.7 on 2023-03-27 16:29

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topicyeucau', '0009_remove_userprofile_fullname_alter_userprofile_course_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/topic')),
            ],
        ),
        migrations.AddField(
            model_name='topic',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/topic'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='TopicSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cus_id', models.CharField(max_length=20)),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topicyeucau.topic')),
            ],
        ),
        migrations.CreateModel(
            name='MyTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cus_id', models.CharField(max_length=20)),
                ('status', models.CharField(default='Chờ tiếp nhận', max_length=20)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topicyeucau.topic')),
            ],
        ),
    ]
