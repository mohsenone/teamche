# Generated by Django 3.1.2 on 2021-03-30 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfd', '0024_classicanalysis_result_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classicanalysis',
            name='result_image_url',
        ),
        migrations.AddField(
            model_name='signal',
            name='result_image_url',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]
