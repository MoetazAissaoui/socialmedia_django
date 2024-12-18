# Generated by Django 4.1.3 on 2024-12-12 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0022_profile_mail_verification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fname',
            field=models.CharField(default='Mr./Mrs.', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lname',
            field=models.CharField(default='Unknown', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(blank=True, default="Can't say", max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(default='Unknown', max_length=100, null=True),
        ),
    ]
