# Generated by Django 3.1.2 on 2022-05-09 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfd', '0067_auto_20220429_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='signal',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='یادداشت'),
        ),
    ]
