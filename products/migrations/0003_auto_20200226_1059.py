# Generated by Django 3.0 on 2020-02-26 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_variation_catagory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='catagory',
            new_name='category',
        ),
    ]
