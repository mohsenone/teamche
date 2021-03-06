# Generated by Django 3.1.2 on 2021-03-06 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0032_auto_20210306_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='base',
            field=models.ForeignKey(blank=True, limit_choices_to={'theme_page__theme__is_active': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='base_page', to='theme.page'),
        ),
    ]
