from django.test import TestCase

from account.forms import UserRegistrationForm, UserEditForm


class AccountFormTestCase(TestCase):

    def setUp(self):
        self.register = \
            {'username': 'test',
             'First_name': 'Test',
             'Last_name': 'Testov',
             'email': 'test@test.ru',
             'password': '1234',
             'password2': '1234'}
        self.register_error = \
            {'username': 'test',
             'First_name': 'Test',
             'Last_name': 'Testov',
             'email': 'test@test.ru',
             'password': '1234',
             'password2': '123'}
        self.edit = \
            {'First_name': 'Testovv'}

    def test_register_form(self):
        """
        Test that we can register with a valid form
        """
        form = UserRegistrationForm(data=self.register)
        self.assertTrue(form.is_valid())

    def test_register_form_error_different_passwords(self):
        """
        Test that we can't register an account with different passwords
        """
        form = UserRegistrationForm(data=self.register_error)
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(Exception, 'Passwords don\'t match.')

    def test_edit_profile_form(self):
        """
        Test that we can edit a user's data
        """
        form = UserEditForm(data=self.edit)
        self.assertTrue(form.is_valid())
