# Generated by Django 3.1.2 on 2021-05-11 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfd', '0042_auto_20210511_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='signal',
            name='self_entered',
            field=models.BooleanField(default=False, verbose_name='وارد شده\u200cاید؟'),
        ),
    ]
