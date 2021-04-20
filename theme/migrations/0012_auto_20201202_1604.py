# Generated by Django 3.1.2 on 2020-12-02 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0011_pagemenu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagemenu',
            name='menu',
        ),
        migrations.AddField(
            model_name='pagemenu',
            name='menu_variable',
            field=models.CharField(default='asdfds', max_length=50, verbose_name='متغیر منو'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='PageMenuContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theme.menu', verbose_name='منو')),
                ('menu_variable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_contents', to='theme.pagemenu', verbose_name='متغیر منو')),
            ],
            options={
                'verbose_name': 'محتوای متغیر منو',
                'verbose_name_plural': 'محتوای متغیرهای منو',
            },
        ),
    ]
