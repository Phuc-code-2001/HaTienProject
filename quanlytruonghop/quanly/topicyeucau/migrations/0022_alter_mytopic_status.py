# Generated by Django 4.1.7 on 2023-04-10 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topicyeucau', '0021_mytopic_start_time_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytopic',
            name='status',
            field=models.CharField(choices=[('Đã tiếp nhận', 'Đã tiếp nhận'), ('Đang xử lý', 'Đang xử lý'), ('Hoàn thành', 'Hoàn thành')], default='Chờ tiếp nhận', max_length=20),
        ),
    ]
