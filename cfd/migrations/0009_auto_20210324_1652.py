# Generated by Django 3.1.2 on 2021-03-24 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfd', '0008_auto_20210324_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classicanalysis',
            name='atr',
            field=models.TextField(blank=True, null=True, verbose_name='ATR'),
        ),
        migrations.AlterField(
            model_name='classicanalysis',
            name='atr_signal',
            field=models.CharField(blank=True, choices=[('by', 'خرید'), ('sl', 'فروش'), ('nt', 'خنثی')], default='nt', max_length=2, null=True, verbose_name='سیگنال دریافتی'),
        ),
        migrations.AlterField(
            model_name='classicanalysis',
            name='atr_timeframe',
            field=models.CharField(blank=True, choices=[('5M', 'M5'), ('15M', 'M15'), ('30M', 'M30'), ('1H', 'H1'), ('4H', 'H4'), ('1D', 'D1'), ('1W', 'W1')], max_length=3, null=True, verbose_name='تایم\u200cفریم'),
        ),
        migrations.AlterField(
            model_name='classicanalysis',
            name='atx',
            field=models.TextField(blank=True, null=True, verbose_name='ATX'),
        ),
        migrations.AlterField(
            model_name='classicanalysis',
            name='atx_signal',
            field=models.CharField(blank=True, choices=[('by', 'خرید'), ('sl', 'فروش'), ('nt', 'خنثی')], default='nt', max_length=2, null=True, verbose_name='سیگنال دریافتی'),
        ),
        migrations.AlterField(
            model_name='classicanalysis',
            name='atx_timeframe',
            field=models.CharField(blank=True, choices=[('5M', 'M5'), ('15M', 'M15'), ('30M', 'M30'), ('1H', 'H1'), ('4H', 'H4'), ('1D', 'D1'), ('1W', 'W1')], max_length=3, null=True, verbose_name='تایم\u200cفریم'),
        ),
    ]
