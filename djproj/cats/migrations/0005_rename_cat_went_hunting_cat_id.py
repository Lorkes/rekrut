# Generated by Django 3.2.8 on 2021-10-24 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0004_user_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hunting',
            old_name='cat_went',
            new_name='cat_id',
        ),
    ]
