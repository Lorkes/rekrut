from django.test import TestCase
from django.core.validators import ValidationError
from rest_framework.test import APIRequestFactory

from .models import User, Cat
from .views import list_users


class UserTest(TestCase):
    def setUp(self):
        u = User.objects.create(user_name='qqq')
        Cat.objects.create(cat_owner=u, cat_name='name', cat_coloration='color', cat_male=True)
        Cat.objects.create(cat_owner=u, cat_name='name', cat_coloration='color', cat_male=True)
        Cat.objects.create(cat_owner=u, cat_name='name', cat_coloration='color', cat_male=True)
        Cat.objects.create(cat_owner=u, cat_name='name', cat_coloration='color', cat_male=True)

    def test_too_many_cats(self):
        """
        It is not possible to assign more than 4 cats to user
        """
        user = User.objects.get(user_name='qqq')
        print(user)
        cat = Cat(cat_owner=user, cat_name="texttexttext1", cat_coloration="color123123123", cat_male=True)
        cat.save()
        with self.assertRaises(ValidationError):
            user.clean_fields()

    def test_user_api_endpoint(self):
        factory = APIRequestFactory()
        request = factory.get('/users/')
        response = list_users(request)
        self.assertEqual(response.data, {'1': {"Name": 'qqq', 'Total cats': 4}})


