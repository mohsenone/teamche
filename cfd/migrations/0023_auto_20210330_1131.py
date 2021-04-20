# Generated by Django 3.1.2 on 2021-03-30 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfd', '0022_auto_20210330_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='classicanalysis',
            name='stochastic_signal',
            field=models.CharField(blank=True, choices=[('by', 'خرید'), ('sl', 'فروش'), ('nt', 'خنثی')], default='nt', max_length=2, null=True, verbose_name='سیگنال دریافتی'),
        ),
        migrations.AddField(
            model_name='classicanalysis',
            name='stochastic_timeframe',
            field=models.CharField(blank=True, choices=[('5M', 'M5'), ('15M', 'M15'), ('30M', 'M30'), ('1H', 'H1'), ('4H', 'H4'), ('1D', 'D1'), ('1W', 'W1')], max_length=3, null=True, verbose_name='تایم\u200cفریم'),
        ),
    ]
