# Generated by Django 3.0.4 on 2020-05-28 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0003_remove_test_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='photo',
            field=models.ImageField(blank=True, upload_to='image'),
        ),
    ]
