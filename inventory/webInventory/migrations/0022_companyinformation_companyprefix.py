# Generated by Django 3.1.1 on 2020-11-26 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webInventory', '0021_usercompany'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinformation',
            name='companyPrefix',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
