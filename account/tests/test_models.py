from django.contrib.auth import get_user_model
from django.test import TestCase


class UserModelTestCase(TestCase):

    def setUp(self):
        self.user_data = {
            'username': 'test',
            'email': 'test@example.com',
            'password': 'test12345',
        }
        get_user_model().objects.create_user(**self.user_data)

    def test_user_to_str(self):
        self.user = get_user_model().objects.first()
        self.assertEqual(str(self.user), f'{self.user.username}')
