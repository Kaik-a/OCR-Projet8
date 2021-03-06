# Generated by Django 3.0.8 on 2020-08-03 11:58

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id_category",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("url", models.URLField()),
            ],
        ),
    ]
