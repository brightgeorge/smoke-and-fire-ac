# Generated by Django 4.1.7 on 2024-01-09 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0010_table_order_no_temp_billing_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='resturant_items',
            name='total_item_wise_amt',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
