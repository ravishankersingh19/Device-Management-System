# Generated by Django 2.1.15 on 2020-09-08 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0005_device_allocation_manager_till_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_allocation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dms.device_allocation_manager', verbose_name='Device Allocation Manager')),
                ('device_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dms.device_manager', verbose_name='Device Manager')),
                ('request_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dms.request_manager', verbose_name='Request Manager')),
            ],
        ),
    ]
