# Generated by Django 3.1.2 on 2020-12-07 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0017_auto_20201207_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagecategory',
            name='count',
            field=models.PositiveSmallIntegerField(default=10, verbose_name='تعداد پست'),
        ),
    ]
