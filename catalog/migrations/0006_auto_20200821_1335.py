# Generated by Django 3.0.8 on 2020-08-21 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_product_nutriments"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="nutriments",
            field=models.CharField(default="", max_length=1000),
        ),
    ]
