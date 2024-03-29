# Generated by Django 4.1.7 on 2024-01-07 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_resturant_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='temp_billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('particulars', models.CharField(max_length=200)),
                ('qty', models.IntegerField()),
                ('amount', models.FloatField()),
                ('kitchen', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('item_catergory', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('table_name', models.CharField(max_length=200)),
                ('day', models.CharField(max_length=200)),
                ('month', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
                ('enter_by', models.CharField(max_length=200)),
                ('cb_date', models.CharField(max_length=200)),
                ('updated_by', models.CharField(max_length=200)),
                ('ub_date', models.CharField(max_length=200)),
                ('deleted_by', models.CharField(max_length=200)),
                ('db_date', models.CharField(max_length=200)),
                ('ub_flag', models.IntegerField()),
                ('flag', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='resturant_items',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
