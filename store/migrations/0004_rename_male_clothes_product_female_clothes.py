# Generated by Django 4.2.7 on 2023-12-14 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_brand_clothes_product_male_clothes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='male_clothes',
            new_name='female_clothes',
        ),
    ]
