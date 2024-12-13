# Generated by Django 4.1 on 2024-12-12 16:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0017_message_room_message_sender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messageroom',
            name='id',
        ),
        migrations.RemoveField(
            model_name='messageroom',
            name='messageroom',
        ),
        migrations.AddField(
            model_name='messageroom',
            name='messageroomid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
