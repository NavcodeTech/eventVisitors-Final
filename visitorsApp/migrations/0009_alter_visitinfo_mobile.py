# Generated by Django 3.2.3 on 2021-06-24 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitorsApp', '0008_alter_visitinfo_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitinfo',
            name='mobile',
            field=models.CharField(max_length=10),
        ),
    ]
