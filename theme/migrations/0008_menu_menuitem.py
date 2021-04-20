# Generated by Django 3.1.2 on 2020-12-02 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0007_pagecategory_pagecategorycontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام منو')),
            ],
            options={
                'verbose_name': 'منو',
                'verbose_name_plural': 'منوها',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='آیتم')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='theme.menu', verbose_name='منو')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submenus', to='theme.menuitem', verbose_name='آیتم والد')),
            ],
            options={
                'verbose_name': 'آیتم منو',
                'verbose_name_plural': 'آیتم\u200cهای منو',
            },
        ),
    ]
