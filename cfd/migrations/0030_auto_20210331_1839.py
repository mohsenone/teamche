# Generated by Django 3.1.2 on 2021-03-31 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfd', '0029_auto_20210331_1545'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classicanalysis',
            old_name='fibo_correction_signal',
            new_name='fibo_signal',
        ),
        migrations.RemoveField(
            model_name='classicanalysis',
            name='fibo_target_signal',
        ),
        migrations.RemoveField(
            model_name='classicanalysis',
            name='macd_trend_breakout',
        ),
        migrations.AlterField(
            model_name='classicanalysis',
            name='atr_signal',
            field=models.CharField(blank=True, choices=[('by', 'خرید'), ('sl', 'فروش'), ('nt', 'خنثی')], max_length=2, null=True, verbose_name='سیگنال دریافتی'),
        ),
        migrations.AlterField(
            model_name='classicanalysis',
            name='atx_signal',
            field=models.CharField(blank=True, choices=[('by', 'خرید'), ('sl', 'فروش'), ('nt', 'خنثی')], max_length=2, null=True, verbose_name='سیگنال دریافتی'),
        ),
        migrations.AlterField(
            model_name='classicanalysis',
            name='eliot',
            field=models.CharField(choices=[('nwv', 'بدون موج'), ('wv1', 'موج اول'), ('wv2', 'موج دوم'), ('wv3', 'موج سوم'), ('wv4', 'موج چهارم'), ('wv5', 'موج پنجم'), ('wva', 'موج A'), ('wvb', 'موج B'), ('wvc', 'موج C')], default='nwv', max_length=3, verbose_name='موج\u200cهای الیوت'),
        ),
        migrations.AlterField(
            model_name='classicanalysis',
            name='image_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='URL تصویر'),
        ),
        migrations.AlterField(
            model_name='classicanalysis',
            name='macd_divergence',
            field=models.BooleanField(default=False, verbose_name='واگرایی'),
        ),
        migrations.AlterField(
            model_name='classicanalysis',
            name='macd_hidden_divergence',
            field=models.BooleanField(default=False, verbose_name='واگرایی مخفی'),
        ),
        migrations.AlterField(
            model_name='classicanalysis',
            name='stochastic_bearish_breakout',
            field=models.BooleanField(default=False, verbose_name='شکست نزولی '),
        ),
        migrations.AlterField(
            model_name='classicanalysis',
            name='stochastic_bullish_breakout',
            field=models.BooleanField(default=False, verbose_name='شکست صعودی '),
        ),
        migrations.AlterField(
            model_name='classicanalysis',
            name='stochastic_overbought',
            field=models.BooleanField(default=False, verbose_name='اشباع خرید'),
        ),
        migrations.AlterField(
            model_name='classicanalysis',
            name='stochastic_oversold',
            field=models.BooleanField(default=False, verbose_name='اشباع فروش'),
        ),
        migrations.AlterField(
            model_name='classicanalysis',
            name='stochastic_signal',
            field=models.CharField(blank=True, choices=[('by', 'خرید'), ('sl', 'فروش'), ('nt', 'خنثی')], max_length=2, null=True, verbose_name='سیگنال دریافتی'),
        ),
    ]
