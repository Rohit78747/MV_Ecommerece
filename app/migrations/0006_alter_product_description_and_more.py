# Generated by Django 4.1.4 on 2022-12-25 09:40

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_product_section_product_image_product_section_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='Product_information',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
