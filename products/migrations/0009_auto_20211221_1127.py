# Generated by Django 3.2 on 2021-12-21 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20211221_1115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='shoe_sizes_man',
            new_name='shoe_size_man',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='shoe_sizes_woman',
            new_name='shoe_size_woman',
        ),
    ]
