# Generated by Django 5.1 on 2024-08-14 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapi', '0006_rename_emloyee_id_emptask_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emptask',
            name='employee_ID',
            field=models.BigIntegerField(default=True, primary_key=True, serialize=False),
        ),
    ]
