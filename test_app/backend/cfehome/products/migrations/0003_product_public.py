# Generated by Django 4.2.2 on 2023-07-03 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_product_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="public",
            field=models.BooleanField(default=True),
        ),
    ]
