# Generated by Django 3.2.4 on 2021-06-30 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitorsApp', '0012_alter_visitinfo_mobile1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitinfo',
            name='mobile1',
            field=models.BigIntegerField(default='null'),
        ),
    ]
