# Generated by Django 3.1.1 on 2021-04-16 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20210404_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workpackage3',
            name='border_color',
            field=models.CharField(default='#f5f5f5', max_length=8),
        ),
    ]
