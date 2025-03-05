# Generated by Django 5.1.5 on 2025-02-24 17:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(max_length=2, unique=True, verbose_name='Plan code')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Plan name')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Plan cost')),
                ('is_active', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(default=datetime.datetime(2025, 2, 24, 17, 9, 21, 570820, tzinfo=datetime.timezone.utc))),
                ('date_changed', models.DateTimeField(default=datetime.datetime(2025, 2, 24, 17, 9, 21, 570835, tzinfo=datetime.timezone.utc))),
                ('description1', models.CharField(max_length=300, verbose_name='Plan Description 1')),
                ('description2', models.CharField(max_length=300, verbose_name='Plan Description 1')),
                ('external_plan_id', models.CharField(max_length=255, unique=True, verbose_name='External plan id')),
                ('external_api_url', models.CharField(max_length=2000, verbose_name='External API url')),
                ('external_style_json', models.CharField(max_length=2000, verbose_name='External style (json)')),
            ],
        ),
        migrations.AlterField(
            model_name='subscription',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Subscription cost'),
        ),
    ]
