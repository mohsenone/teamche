# Generated by Django 3.1.2 on 2021-03-31 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfd', '0027_auto_20210331_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classicanalysis',
            name='eliot_signal',
            field=models.CharField(choices=[('by', 'خرید'), ('sl', 'فروش'), ('nt', 'خنثی')], default='nt', max_length=2, verbose_name='سیگنال دریافتی'),
        ),
    ]
