from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, ValidationError


class User(models.Model):
    user_name = models.CharField(max_length=100)
    user_total_cats = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(4)])


def limit_cats(value):
    if Cat.objects.filter(cat_owner_id=value).count() >= 4:
        raise ValidationError('User already has maximum amount of cats (4)')


class Cat(models.Model):
    cat_owner = models.ForeignKey(User, on_delete=models.CASCADE, validators=(limit_cats,), related_name='cats')
    cat_name = models.CharField(max_length=100)
    cat_coloration = models.CharField(max_length=200)
    cat_male = models.BooleanField(choices=[(True, '✅'), (False, '❌')], default=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.cat_owner.user_total_cats = self.cat_owner.cats.count()
        self.cat_owner.save()


class Hunting(models.Model):
    cat_went = models.ForeignKey(Cat, on_delete=models.CASCADE)
    hunting_duration = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(72)]) # 1 hour - 3 days
    hunting_prey = models.CharField(max_length=100)

