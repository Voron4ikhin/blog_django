# Generated by Django 4.0.2 on 2022-02-21 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Arcticle',
            new_name='Article',
        ),
    ]
