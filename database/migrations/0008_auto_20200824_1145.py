# Generated by Django 3.0.8 on 2020-08-24 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_auto_20200821_1337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='nutrution_grade',
            new_name='nutrution_grade_fr',
        ),
    ]
