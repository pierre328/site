# Generated by Django 3.1.6 on 2021-12-14 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20211214_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(blank=True, height_field='100', upload_to='blog'),
        ),
    ]
