# Generated by Django 4.0.3 on 2022-03-18 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventorymicroservice', '0002_remove_bookinventory_inventory_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinventory',
            old_name='book_id',
            new_name='book_number',
        ),
    ]