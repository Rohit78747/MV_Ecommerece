# Generated by Django 4.1.4 on 2022-12-25 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='media/slider_images')),
                ('Discount_Deal', models.CharField(choices=[('HOT DEALS', 'HOT DEALS'), ('New Arraivels', 'New Arraivels')], max_length=100)),
                ('SALE', models.IntegerField()),
                ('Brand_Name', models.CharField(max_length=100)),
                ('Discount', models.IntegerField()),
                ('Link', models.CharField(max_length=200)),
            ],
        ),
    ]