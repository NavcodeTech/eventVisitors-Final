# Generated by Django 3.2.4 on 2021-07-01 15:27

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('visitorsApp', '0013_alter_visitinfo_mobile1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitinfo',
            name='mobile1',
            field=phonenumber_field.modelfields.PhoneNumberField(default='null', max_length=128, region=None),
        ),
    ]
