# Generated by Django 3.1.1 on 2020-11-28 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webInventory', '0022_companyinformation_companyprefix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinformation',
            name='companyPrefix',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]
