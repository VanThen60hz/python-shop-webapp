# Generated by Django 4.2.7 on 2023-12-14 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_digital_product_brand_clothes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='brand_clothes',
            new_name='male_clothes',
        ),
    ]
