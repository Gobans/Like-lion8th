# Generated by Django 3.0.4 on 2020-06-30 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200630_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='productId',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='productPrice',
        ),
    ]
