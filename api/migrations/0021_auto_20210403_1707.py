# Generated by Django 3.1.1 on 2021-04-03 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20210403_1706'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='create_by',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='workpackage0',
            old_name='create_by',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='workpackage1',
            old_name='create_by',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='workpackage2',
            old_name='create_by',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='workpackage3',
            old_name='create_by',
            new_name='created_by',
        ),
    ]