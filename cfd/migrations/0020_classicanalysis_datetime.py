# Generated by Django 3.1.2 on 2021-03-30 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfd', '0019_auto_20210330_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='classicanalysis',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
