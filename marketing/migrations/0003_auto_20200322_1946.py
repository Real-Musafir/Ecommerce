# Generated by Django 3.0 on 2020-03-22 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0002_auto_20200322_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketingmessage',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
