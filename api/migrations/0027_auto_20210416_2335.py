# Generated by Django 3.1.1 on 2021-04-16 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_auto_20210416_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workpackage3',
            name='title',
            field=models.CharField(default='Untitled', max_length=255),
        ),
    ]
