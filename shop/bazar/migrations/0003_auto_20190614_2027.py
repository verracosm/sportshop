# Generated by Django 2.2.2 on 2019-06-14 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazar', '0002_auto_20190614_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
