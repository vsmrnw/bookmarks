from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


class AccountAppTestCase(TestCase):
    def setUp(self):
        self.credentials_username = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials_username)
        self.credentials_email = {
            'username': 'testuser@test.ru',
            'password': 'secret'
        }

        self.client = Client()
        self.register = reverse('register')
        self.login = reverse('login')
        self.logout = reverse('logout')

    def test_get_register_view(self):
        """
        Test that we can get register view correctly
        """
        response = self.client.get(path=self.register)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/register.html')

    def test_user_created(self):
        """
        Test that user was successfully created
        """
        user = User.objects.filter(
            username=self.credentials_username['username'])
        self.assertTrue(user.exists())

    def test_get_login_view(self):
        """
        Test that we can get login template
        """
        response = self.client.get(path=self.login)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_post_login_by_username(self):
        """
        Test that we can log in correctly by username
        """
        response = self.client.post(path=self.login,
                                    data=self.credentials_username)
        self.assertEqual(response.status_code, 302)

    def test_post_login_by_email(self):
        """
        Test that we can log in correctly by email
        """
        response = self.client.post(path=self.login,
                                    data=self.credentials_email)
        self.assertEqual(response.status_code, 200)

    def test_redirect_if_not_logged_in(self):
        """
        Test that we can redirect if not logged in
        """
        response = self.client.get(reverse('dashboard'))
        self.assertRedirects(response, '/account/login/?next=/account/')

    def test_logout_view(self):
        """
        Test that we can log out correctly
        """
        response = self.client.post(self.logout, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_post_register_view_with_email_existed(self):
        """
        Test that we can't register with existed email
        """
        get_user_model().objects.create_user(**self.credentials_email)
        response = self.client.post(path=self.register,
                                    data=self.credentials_email)
        self.assertFormError(response, 'form', 'email',
                             'Email already in use.')
