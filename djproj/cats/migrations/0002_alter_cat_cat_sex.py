# Generated by Django 3.2.8 on 2021-10-24 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='cat_sex',
            field=models.BooleanField(choices=[(True, '✅'), (False, '❌')], default=True),
        ),
    ]
