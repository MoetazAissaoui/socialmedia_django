# Generated by Django 4.1 on 2024-12-12 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0012_profile_joining'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='file',
            field=models.ImageField(default='defaultprofile.jpg', upload_to='images'),
        ),
    ]
