# Generated by Django 3.1.2 on 2021-03-23 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfd', '0004_auto_20210324_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ptaanalysis',
            name='news_detail',
            field=models.TextField(blank=True, help_text='توجه: سه دقیقه قبل و بعد از خبر نباید وارد معامله شوید، اما در صورتی که برای انجام معامله مصر هستید، اطلاعات خبر را اینجا وارد کنید.', null=True, verbose_name='جزئیات خبر'),
        ),
        migrations.AlterField(
            model_name='signal',
            name='trade_id',
            field=models.CharField(blank=True, help_text='مشخصه\u200cای که با آن بتوان معامله را در پلتفرم\u200cهای معاملاتی پیدا کرد', max_length=100, null=True, verbose_name='شناسه Trade'),
        ),
    ]
