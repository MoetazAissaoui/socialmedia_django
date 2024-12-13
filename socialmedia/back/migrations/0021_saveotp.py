# Generated by Django 4.1.3 on 2024-12-12 07:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0020_messageroom_lastmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='saveotp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('when', models.DateTimeField(default=datetime.datetime.now)),
                ('otp', models.CharField(max_length=8)),
            ],
        ),
    ]
