# Generated by Django 3.1.1 on 2020-09-28 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webInventory', '0010_item_sku'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='created_by_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
