# Generated by Django 3.2.8 on 2021-10-24 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0003_rename_cat_sex_update_cat_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_name',
            field=models.CharField(default='javk', max_length=100),
            preserve_default=False,
        ),
    ]
