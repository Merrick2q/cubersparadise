# Generated by Django 4.2.5 on 2023-09-12 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_product_description_alter_product_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Items',
        ),
    ]