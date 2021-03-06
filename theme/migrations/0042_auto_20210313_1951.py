# Generated by Django 3.1.2 on 2021-03-13 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0041_auto_20210313_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetting',
            name='accend_bold_color',
            field=models.CharField(blank=True, default='', max_length=6, null=True, verbose_name='رنگ فرعی پررنگ'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='accend_dark_color',
            field=models.CharField(blank=True, default='', max_length=6, null=True, verbose_name='رنگ فرعی تیره'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='accend_light_color',
            field=models.CharField(blank=True, default='', max_length=6, null=True, verbose_name='رنگ فرعی'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='primary_bold_color',
            field=models.CharField(blank=True, default='', max_length=6, null=True, verbose_name='رنگ اصلی پررنگ'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='primary_dark_color',
            field=models.CharField(blank=True, default='', max_length=6, null=True, verbose_name='رنگ اصلی تیره'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='primary_light_color',
            field=models.CharField(blank=True, default='', max_length=6, null=True, verbose_name='رنگ اصلی'),
        ),
    ]
