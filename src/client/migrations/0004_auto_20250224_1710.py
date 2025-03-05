# Generated by Django 5.1.5 on 2025-02-24 17:10

from django.db import migrations, models
import django.utils.timezone

def populate_plan_choice(apps,schema_editor):
    PlanChoice = apps.get_model('client', 'PlanChoice')
    PlanChoice.objects.create(
        plan='ST',
        name='Standard',
        cost='3.00',
        is_active=True,
        description1='Get access to standard articles and reports',
        description2='Limited access',
        external_plan_id='P-5CY6753525879563JM64K4QI',
        external_api_url='https://www.paypal.com/sdk/js?client-id=AZCjz0GNxeZ0eTmrINTYfcqwpev9cuJhRGCVyOatDOpcFdhsvVUmQGoTt1wLYlgfZwe_g3zQ8Is80KGG&vault=true&intent=subscription',
        external_style_json="""{
        "shape": "pill",
        "color": "blue",
        "layout": "vertical",
        "label": "subscribe"
        }"""
    )
    PlanChoice.objects.create(
        plan='PR',
        name='Premium',
        cost='9.00',
        is_active=True,
        description1='Highly regarded premium articles and reports',
        description2='Full Access',
        external_plan_id='P-23435713LA1089155M64LEGA',
        external_api_url='https://www.paypal.com/sdk/js?vault=true&intent=subscription',
        external_style_json="""{
        "shape": "pill",
        "color": "gold",
        "layout": "vertical",
        "label": "subscribe"
        }"""
    )

class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_alter_planchoice_date_added_and_more'),
    ]

    operations = [
        migrations.RunPython(populate_plan_choice),
    ]
