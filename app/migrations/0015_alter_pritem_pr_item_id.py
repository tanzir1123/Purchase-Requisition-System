# Generated by Django 4.1.3 on 2023-01-26 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_financeofficer_user_purchaser_user_vendor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pritem',
            name='pr_item_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
