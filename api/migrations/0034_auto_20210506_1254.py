# Generated by Django 3.1.1 on 2021-05-06 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_workpackage3_inputfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workpackage3',
            name='inputFile',
            field=models.FileField(blank=True, upload_to='documents/'),
        ),
    ]