# Generated by Django 3.1.2 on 2020-12-09 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0019_auto_20201209_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagecategory',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_categories', to='theme.page', verbose_name='صفحه'),
        ),
        migrations.AlterField(
            model_name='pagepost',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_posts', to='theme.page', verbose_name='صفحه'),
        ),
    ]
