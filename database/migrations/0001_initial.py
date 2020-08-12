# Generated by Django 3.0.8 on 2020-08-03 09:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('brands', models.CharField(max_length=100)),
                ('category_tags', models.CharField(max_length=500)),
                ('nutrution_grade', models.CharField(max_length=1)),
                ('product_name_fr', models.CharField(max_length=100)),
                ('url_img', models.URLField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('id_substitued', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_product_substitued', to='database.Product')),
                ('id_substitute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_product_substitute', to='database.Product')),
            ],
        ),
    ]
