# Generated by Django 4.0.3 on 2022-03-18 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventorymicroservice', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinventory',
            name='inventory_id',
        ),
        migrations.AlterField(
            model_name='bookinventory',
            name='count',
            field=models.IntegerField(),
        ),
    ]
