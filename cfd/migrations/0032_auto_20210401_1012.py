# Generated by Django 3.1.2 on 2021-04-01 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cfd', '0031_auto_20210401_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signal',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signals', to='cfd.asset', verbose_name='دارایی'),
        ),
    ]
