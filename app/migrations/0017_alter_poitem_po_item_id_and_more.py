# Generated by Django 4.1.3 on 2023-01-26 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_quotation_purchaser_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poitem',
            name='po_item_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='quotationitem',
            name='q_item_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
