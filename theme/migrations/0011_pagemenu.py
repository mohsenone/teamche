# Generated by Django 3.1.2 on 2020-12-02 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0010_auto_20201202_1211'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_menus', to='theme.menu', verbose_name='منو')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menus', to='theme.page', verbose_name='صفحه')),
            ],
            options={
                'verbose_name': 'منو صفحه',
                'verbose_name_plural': 'منوهای صفحه',
            },
        ),
    ]
