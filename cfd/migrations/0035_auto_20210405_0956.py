# Generated by Django 3.1.2 on 2021-04-05 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfd', '0034_auto_20210405_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classicanalysis',
            name='title',
            field=models.CharField(max_length=70, verbose_name='عنوان'),
        ),
    ]
