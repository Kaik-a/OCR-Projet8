# Generated by Django 3.1.1 on 2020-09-07 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0010_auto_20200907_1130"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_name_fr",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
