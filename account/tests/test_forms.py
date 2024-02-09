from django.test import TestCase

from account.forms import UserRegistrationForm


class AccountFormTestCase(TestCase):

    def setUp(self):
        self.register_error = \
                    {'username': 'test',
                     'First_name': 'Test',
                     'Last_name': 'Testov',
                     'email': 'test@test.ru',
                     'password': '1234',
                     'password2': '123'}
        self.register = \
                    {'username': 'test',
                     'First_name': 'Test',
                     'Last_name': 'Testov',
                     'email': 'test@test.ru',
                     'password': '1234',
                     'password2': '1234'}
        self.edit = {'First_name': 'Testovv'}

    def test_register_form_error_different_passwords(self):
        form = UserRegistrationForm(data=self.register_error)
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(Exception, 'Passwords don\'t match.')

    def test_register_form(self):
        form = UserRegistrationForm(data=self.register)
        self.assertTrue(form.is_valid())

