# Generated by Django 3.2 on 2021-04-13 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0007_alter_meeting_proceedings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetingsigature',
            name='read',
        ),
        migrations.RemoveField(
            model_name='meetingsigature',
            name='view_date',
        ),
    ]
