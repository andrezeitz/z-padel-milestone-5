# Generated by Django 3.2 on 2022-01-26 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_alter_review_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
    ]
