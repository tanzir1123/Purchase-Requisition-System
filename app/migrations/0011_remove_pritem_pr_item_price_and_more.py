# Generated by Django 4.1.3 on 2023-01-25 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_manager_manager_name_manager_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pritem',
            name='pr_item_price',
        ),
        migrations.RemoveField(
            model_name='pritem',
            name='pr_item_unit_price',
        ),
    ]