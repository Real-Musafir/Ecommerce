# Generated by Django 3.0 on 2020-03-11 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200311_1757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailconfirmed',
            old_name='hashkey',
            new_name='activation_key',
        ),
    ]
