# Generated by Django 3.2.3 on 2021-06-23 16:15

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('visitorsApp', '0007_alter_visitinfo_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitinfo',
            name='mobile',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
