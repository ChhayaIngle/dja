# Generated by Django 5.1 on 2024-08-12 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_picture'),
        ),
    ]
