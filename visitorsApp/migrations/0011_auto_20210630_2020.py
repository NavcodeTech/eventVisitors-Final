# Generated by Django 3.2.3 on 2021-06-30 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitorsApp', '0010_auto_20210624_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitinfo',
            name='mobile2',
        ),
        migrations.AlterField(
            model_name='visitinfo',
            name='mobile1',
            field=models.CharField(default='null', max_length=10),
        ),
    ]
