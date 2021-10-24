from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class User(models.Model):
    user_total_cats = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(4)])


class Cat(models.Model):
    cat_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    cat_name = models.CharField(max_length=100)
    cat_coloration = models.CharField(max_length=200)
    cat_sex = models.BooleanField(choices=[(True, '✅'), (False, '❌')], default=True)


class Hunting(models.Model):
    cat_went = models.ForeignKey(Cat, on_delete=models.CASCADE)
    hunting_duration = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(72)]) # 1 hour - 3 days
    hunting_prey = models.CharField(max_length=100)

