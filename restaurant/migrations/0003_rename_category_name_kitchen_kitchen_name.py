# Generated by Django 4.1.7 on 2024-01-07 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_kitchen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kitchen',
            old_name='category_name',
            new_name='kitchen_name',
        ),
    ]