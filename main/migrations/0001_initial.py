# Generated by Django 5.0.1 on 2024-02-05 14:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.TextField(verbose_name='plan')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'plan',
            },
        ),
        migrations.CreateModel(
            name='ScheduleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.TextField(max_length=32, unique=True, verbose_name='uuid')),
                ('schedule_name', models.CharField(max_length=50, verbose_name='schedule_name')),
                ('schedule_info', models.TextField(max_length=500, verbose_name='schedule_info')),
                ('created_time', models.TextField(max_length=10, verbose_name='created_time')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'schedule',
            },
        ),
    ]
