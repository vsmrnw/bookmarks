from django.test import TestCase

from account.forms import UserRegistrationForm


class AccountFormTestCase(TestCase):

    def setUp(self):
        self.register = {'username': 'test',
                     'First_name': 'Test',
                     'Last_name': 'Testov',
                     'email': 'test@test.ru',
                     'password': '1234',
                     'password2': '123'}

    def test_register_form_error(self):
        form = UserRegistrationForm(data=self.register)
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(Exception, 'Passwords don\'t match.')
