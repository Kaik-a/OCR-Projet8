# Generated by Django 3.0.8 on 2020-08-04 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_favorite_id_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorite',
            old_name='id_substitued',
            new_name='substitued',
        ),
        migrations.RenameField(
            model_name='favorite',
            old_name='id_substitute',
            new_name='substitute',
        ),
        migrations.RenameField(
            model_name='favorite',
            old_name='id_user',
            new_name='user',
        ),
    ]
