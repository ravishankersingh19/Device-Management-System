# Generated by Django 2.1.15 on 2020-09-07 11:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0004_auto_20200907_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='device_allocation_manager',
            name='till_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Till Date'),
            preserve_default=False,
        ),
    ]