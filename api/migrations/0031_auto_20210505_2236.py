# Generated by Django 3.1.1 on 2021-05-05 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_auto_20210418_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workpackage1',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='workpackage1',
            name='project',
        ),
        migrations.RemoveField(
            model_name='workpackage1',
            name='responsible',
        ),
        migrations.RemoveField(
            model_name='workpackage1',
            name='state',
        ),
        migrations.RemoveField(
            model_name='workpackage1',
            name='workPackage',
        ),
        migrations.RemoveField(
            model_name='workpackage2',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='workpackage2',
            name='project',
        ),
        migrations.RemoveField(
            model_name='workpackage2',
            name='responsible',
        ),
        migrations.RemoveField(
            model_name='workpackage2',
            name='state',
        ),
        migrations.RemoveField(
            model_name='workpackage2',
            name='workPackage',
        ),
        migrations.RemoveField(
            model_name='workpackage3',
            name='workPackage',
        ),
        migrations.AlterField(
            model_name='userprofiledetail',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.DeleteModel(
            name='WorkPackage0',
        ),
        migrations.DeleteModel(
            name='WorkPackage1',
        ),
        migrations.DeleteModel(
            name='WorkPackage2',
        ),
    ]