# Generated by Django 3.1.2 on 2021-06-23 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dmo', '0011_auto_20210623_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='dmo_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='مدیر DMO'),
        ),
    ]
