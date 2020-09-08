# Generated by Django 2.1.15 on 2020-09-07 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0002_request_manager_till_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device_allocation_manager',
            name='assign_employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pms.TblUser', verbose_name='Assign Device Person Name'),
        ),
    ]