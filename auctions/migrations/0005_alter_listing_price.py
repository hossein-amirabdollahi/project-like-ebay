# Generated by Django 5.1 on 2024-11-28 10:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0004_bid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="price",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bidPrice",
                to="auctions.bid",
            ),
        ),
    ]