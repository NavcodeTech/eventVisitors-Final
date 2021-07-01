# Generated by Django 3.2.3 on 2021-06-23 04:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitorsApp', '0003_meetinginfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetinginfo',
            name='attendee',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='meetinginfo',
            name='depart',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='meetinginfo',
            name='feedback',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='meetinginfo',
            name='organiser',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='meetinginfo',
            name='summary',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='visitinfo',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='visitinfo',
            name='department',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='visitinfo',
            name='mobile',
            field=models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='visitinfo',
            name='purpose',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='visitinfo',
            name='vname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='visitinfo',
            name='whom',
            field=models.CharField(max_length=20),
        ),
    ]