# Generated by Django 3.2.8 on 2021-10-24 13:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=100)),
                ('cat_coloration', models.CharField(max_length=200)),
                ('cat_sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_total_cats', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
            ],
        ),
        migrations.CreateModel(
            name='Hunting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hunting_duration', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(72)])),
                ('hunting_prey', models.CharField(max_length=100)),
                ('cat_went', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cats.cat')),
            ],
        ),
        migrations.AddField(
            model_name='cat',
            name='cat_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cats.user'),
        ),
    ]
