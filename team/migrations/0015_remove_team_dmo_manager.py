# Generated by Django 3.1.2 on 2021-06-23 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0014_team_dmo_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='dmo_manager',
        ),
    ]
