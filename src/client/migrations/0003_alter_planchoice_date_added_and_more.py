# Generated by Django 5.1.5 on 2025-02-24 17:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_planchoice_alter_subscription_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planchoice',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='planchoice',
            name='date_changed',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
