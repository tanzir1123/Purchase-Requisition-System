# Generated by Django 4.1.3 on 2023-01-23 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_financeofficer_manager_pr_purchaser_vendor_pritem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='vendor_contact',
            field=models.CharField(default=True, max_length=15, null=True),
        ),
    ]
