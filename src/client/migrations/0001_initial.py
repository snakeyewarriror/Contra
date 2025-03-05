# Generated by Django 5.1.5 on 2025-02-18 17:08

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
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(choices=[('ST', 'Standard'), ('PR', 'Premium')], default='ST', max_length=2)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Cost')),
                ('payment_provider_id', models.CharField(max_length=255, verbose_name='Payment Provider ID')),
                ('is_active', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
