# Generated by Django 4.1 on 2024-12-12 15:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0011_rename_image_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='joining',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
