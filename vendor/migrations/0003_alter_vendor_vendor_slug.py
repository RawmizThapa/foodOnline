# Generated by Django 4.1.1 on 2022-10-30 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_vendor_vendor_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='vendor_slug',
            field=models.SlugField(unique=True),
        ),
    ]