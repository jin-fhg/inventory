# Generated by Django 2.2.4 on 2020-09-18 21:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('webInventory', '0004_auto_20200919_0511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audittrail',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 18, 21, 53, 18, 12699, tzinfo=utc)),
        ),
    ]
