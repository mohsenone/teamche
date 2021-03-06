# Generated by Django 3.1.2 on 2021-03-28 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfd', '0015_auto_20210328_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signal',
            name='entry_point1',
            field=models.DecimalField(decimal_places=4, max_digits=11, verbose_name='نقطه ورود اول'),
        ),
        migrations.AlterField(
            model_name='signal',
            name='entry_point2',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=11, null=True, verbose_name='نقطه ورود دوم'),
        ),
        migrations.AlterField(
            model_name='signal',
            name='stop_loss1',
            field=models.DecimalField(decimal_places=4, max_digits=11, verbose_name='حد ضرر اول'),
        ),
        migrations.AlterField(
            model_name='signal',
            name='stop_loss2',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=11, null=True, verbose_name='حد ضرر دوم'),
        ),
        migrations.AlterField(
            model_name='signal',
            name='take_profit1',
            field=models.DecimalField(decimal_places=4, max_digits=11, verbose_name='حد سود اول'),
        ),
        migrations.AlterField(
            model_name='signal',
            name='take_profit2',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=11, null=True, verbose_name='حد سود دوم'),
        ),
        migrations.AlterField(
            model_name='signal',
            name='take_profit3',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=11, null=True, verbose_name='حد سود سوم'),
        ),
    ]
