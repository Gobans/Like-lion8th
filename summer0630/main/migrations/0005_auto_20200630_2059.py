# Generated by Django 3.0.4 on 2020-06-30 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200630_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='memberId',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='productName',
        ),
        migrations.RemoveField(
            model_name='sheets',
            name='GoodsId',
        ),
    ]
