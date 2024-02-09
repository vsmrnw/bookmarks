from django.contrib.auth import get_user
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


class AccountAppTestCase(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)

        self.client = Client()
        self.login = reverse('login')
        self.logout = reverse('logout')

    def test_user_created(self):
        """
        Test that user was successfully created
        """
        user = User.objects.filter(username=self.credentials['username'])
        self.assertTrue(user.exists())

    def test_get_login_view(self):
        """
        Test that we can get login template
        """
        response = self.client.get(path=self.login)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_post_login_view(self):
        """
        Test that we can login correctly
        """
        response = self.client.post(path=self.login,
                                    data=self.credentials)
        self.assertEqual(response.status_code, 302)

    def test_redirect_if_not_logged_in(self):
        """
        Test that we can redirect if not logged in
        """
        response = self.client.get(reverse('dashboard'))
        self.assertRedirects(response, '/account/login/?next=/account/')
