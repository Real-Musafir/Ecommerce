# Generated by Django 3.0 on 2020-02-25 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_variation_catagory'),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, null=True, to='products.Variation'),
        ),
    ]
