# Generated by Django 3.2 on 2022-01-10 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='default_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]