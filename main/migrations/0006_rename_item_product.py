# Generated by Django 4.2.5 on 2023-09-19 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_item_delete_items'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Item',
            new_name='Product',
        ),
    ]
