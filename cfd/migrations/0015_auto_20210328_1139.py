# Generated by Django 3.1.2 on 2021-03-28 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfd', '0014_auto_20210328_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signal',
            name='entry_point1',
            field=models.DecimalField(decimal_places=4, max_digits=13, verbose_name='نقطه ورود اول'),
        ),
        migrations.AlterField(
            model_name='signal',
            name='entry_point2',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=13, null=True, verbose_name='نقطه ورود دوم'),
        ),
        migrations.AlterField(
            model_name='signal',
            name='risk_reward',
            field=models.DecimalField(decimal_places=2, max_digits=4, verbose_name='نسبت سود به ضرر'),
        ),
        migrations.AlterField(
            model_name='signal',
            name='stop_loss1',
            field=models.DecimalField(decimal_places=4, max_digits=13, verbose_name='حد ضرر اول'),
        ),
        migrations.AlterField(
            model_name='signal',
            name='stop_loss2',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=13, null=True, verbose_name='حد ضرر دوم'),
        ),
        migrations.AlterField(
            model_name='signal',
            name='take_profit1',
            field=models.DecimalField(decimal_places=4, max_digits=13, verbose_name='حد سود اول'),
        ),
        migrations.AlterField(
            model_name='signal',
            name='take_profit2',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=13, null=True, verbose_name='حد سود دوم'),
        ),
        migrations.AlterField(
            model_name='signal',
            name='take_profit3',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=13, null=True, verbose_name='حد سود سوم'),
        ),
    ]
