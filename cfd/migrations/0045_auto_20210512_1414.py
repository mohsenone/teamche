# Generated by Django 3.1.2 on 2021-05-12 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfd', '0044_auto_20210511_1854'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classicanalysis',
            old_name='atx_signal',
            new_name='adx_signal',
        ),
        migrations.RenameField(
            model_name='classicanalysis',
            old_name='atx_timeframe',
            new_name='adx_timeframe',
        ),
        migrations.RemoveField(
            model_name='classicanalysis',
            name='atx',
        ),
        migrations.AddField(
            model_name='classicanalysis',
            name='adx',
            field=models.TextField(blank=True, null=True, verbose_name='ADX'),
        ),
        migrations.AlterField(
            model_name='classicanalysis',
            name='fibo_target',
            field=models.CharField(choices=[('nt', 'بدون هدف'), ('23', '23.6%'), ('38', '38.2%'), ('50', '50%'), ('61', '61.8%'), ('74', '74%'), ('127', '127%'), ('150', '150%'), ('161', '161.8%'), ('200', '200%'), ('261', '261.8%'), ('423', '423.6%')], default='nt', max_length=3, verbose_name='هدف فیبوناچی'),
        ),
        migrations.AlterField(
            model_name='ptaanalysis',
            name='chart_move',
            field=models.CharField(choices=[('imp', 'Impulsive'), ('cor', 'Corrective')], default='imp', max_length=3, verbose_name='حرکت نمودار'),
        ),
        migrations.AlterField(
            model_name='ptaanalysis',
            name='scenario',
            field=models.CharField(choices=[('sc1', 'سناریو شماره 1'), ('sc2', 'سناریو شماره 2'), ('sc3', 'سناریو شماره 3'), ('sc4', 'سناریو شماره 4'), ('sc5', 'سناریو شماره 5')], default='sc3', max_length=3, verbose_name='سناریو'),
        ),
        migrations.AlterField(
            model_name='ptaanalysis',
            name='zone_rejects',
            field=models.PositiveSmallIntegerField(default=3, help_text='تعداد برخورد و بازگشت قیمت از ناحیه را مشخص کنید ', verbose_name='مقاومت ناحیه'),
        ),
    ]
