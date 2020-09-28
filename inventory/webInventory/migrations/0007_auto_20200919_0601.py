# Generated by Django 2.2.4 on 2020-09-18 22:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webInventory', '0006_auto_20200919_0554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audittrail',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='item',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='itemfolder',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='tag',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
