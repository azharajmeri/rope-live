# Generated by Django 3.1.1 on 2021-04-16 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20210416_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workpackage3',
            name='title',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
