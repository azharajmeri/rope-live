# Generated by Django 3.1.1 on 2021-03-29 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20210328_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workpackage0',
            name='date_of_state1',
        ),
        migrations.RemoveField(
            model_name='workpackage0',
            name='date_of_state2',
        ),
        migrations.RemoveField(
            model_name='workpackage0',
            name='date_of_state3',
        ),
        migrations.RemoveField(
            model_name='workpackage0',
            name='date_of_state4',
        ),
        migrations.RemoveField(
            model_name='workpackage1',
            name='date_of_state1',
        ),
        migrations.RemoveField(
            model_name='workpackage1',
            name='date_of_state2',
        ),
        migrations.RemoveField(
            model_name='workpackage1',
            name='date_of_state3',
        ),
        migrations.RemoveField(
            model_name='workpackage1',
            name='date_of_state4',
        ),
        migrations.RemoveField(
            model_name='workpackage2',
            name='date_of_state1',
        ),
        migrations.RemoveField(
            model_name='workpackage2',
            name='date_of_state2',
        ),
        migrations.RemoveField(
            model_name='workpackage2',
            name='date_of_state3',
        ),
        migrations.RemoveField(
            model_name='workpackage2',
            name='date_of_state4',
        ),
        migrations.RemoveField(
            model_name='workpackage3',
            name='date_of_state1',
        ),
        migrations.RemoveField(
            model_name='workpackage3',
            name='date_of_state2',
        ),
        migrations.RemoveField(
            model_name='workpackage3',
            name='date_of_state3',
        ),
        migrations.RemoveField(
            model_name='workpackage3',
            name='date_of_state4',
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.state')),
                ('user_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.usertype')),
            ],
        ),
    ]
