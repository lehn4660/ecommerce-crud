# Generated by Django 4.1.7 on 2023-04-04 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_alter_addproducts_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='addproducts',
            name='image',
            field=models.ImageField(default='', upload_to='products/'),
        ),
    ]
