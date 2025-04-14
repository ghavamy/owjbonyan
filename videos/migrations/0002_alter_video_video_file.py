# Generated by Django 4.2.3 on 2025-04-11 11:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(upload_to='uploads/video_files', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mkv'])]),
        ),
    ]
