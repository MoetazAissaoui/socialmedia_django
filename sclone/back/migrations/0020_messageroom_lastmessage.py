# Generated by Django 4.1 on 2022-09-21 12:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0019_rename_message_cmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='messageroom',
            name='lastmessage',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]