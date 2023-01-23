# Generated by Django 4.1.3 on 2023-01-23 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='employeeId',
            new_name='employee_id',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='employeeName',
            new_name='employee_name',
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_contact',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
