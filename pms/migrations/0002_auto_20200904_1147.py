# Generated by Django 2.1.15 on 2020-09-04 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PmsTblcountry',
        ),
        migrations.DeleteModel(
            name='PmsTblcurency',
        ),
        migrations.DeleteModel(
            name='PmsTbldepartment',
        ),
        migrations.DeleteModel(
            name='PmsTblemployees',
        ),
        migrations.DeleteModel(
            name='PmsTblemployeetechnologies',
        ),
        migrations.DeleteModel(
            name='PmsTblflag',
        ),
        migrations.DeleteModel(
            name='PmsTblholidays',
        ),
        migrations.DeleteModel(
            name='PmsTbllockedresource',
        ),
        migrations.DeleteModel(
            name='PmsTblsettings',
        ),
        migrations.DeleteModel(
            name='PmsTbltechnologies',
        ),
        migrations.DeleteModel(
            name='PmsTbluser',
        ),
        migrations.DeleteModel(
            name='PmsTbluserlog',
        ),
        migrations.DeleteModel(
            name='PmsTblusertype',
        ),
    ]