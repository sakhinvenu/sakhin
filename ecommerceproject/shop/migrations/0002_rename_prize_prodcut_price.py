# Generated by Django 3.2.5 on 2021-07-26 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prodcut',
            old_name='prize',
            new_name='price',
        ),
    ]
