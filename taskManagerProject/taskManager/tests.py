from django.test import TestCase, SimpleTestCase

from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from rest_framework import status

from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.

def create_user(**params):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test the public features of the user API."""

    def setUp(self):
        self.client = APIClient()
        self.registerURL = reverse("ApiRegisterView_name")

    def test_create_user_success(self):
        """Test creating a user is successful."""
        payload = {
            'email': 'test@example.com',
            'name': 'Test Name',
            'surname': 'Test Surname',
            'password': 'testpass123',
        }
        res = self.client.post(self.registerURL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_with_email_exists_error(self):
        """Test error returned if user with email exists."""
        payload = {
            'email': 'test@example.com',
            'name': 'Test Name',
            'surname': 'Test Surname',
            'password': 'testpass123',
        }
        create_user(**payload)
        res = self.client.post(self.registerURL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

class PublicLoginApiTests(TestCase):
    """Tests the login functionality of the API"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email = "test@example.com",
            name = "name",
            surname = "surname",
            password = "testpass123",
        )
        self.login_url = reverse("ApiLoginView_name")

    def test_login_success(self):
        """Test logging in with valid credentials"""
        payload = {
            "username":self.user.email,
            "password":"testpass123",
        }

        result = self.client.post(self.login_url, payload)

        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertIn("token", result.data)

    def test_login_with_invalid_credentials(self):
        """Test logging in with invalid credentials"""
        payload = {
            "username":"wrong@example.com",
            "password":"wrongpass123",
        }

        result = self.client.post(self.login_url, payload)

        self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn("password", result.data)
        self.assertNotIn("token", result.data)

    def test_login_with_non_existent_user(self):
        """Test logging in with non-existent credentials"""
        payload = {
            "username":"nonExistent@example.com",
            "password":"nonExistent123",
        }

        result = self.client.post(self.login_url, payload)

        self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn("password", result.data)
        self.assertNotIn("token", result.data)

    def test_login_with_blank_credentials(self):
        """Test logging in with blank credentials"""
        payload = {
            "username": "",
            "password": "",
        }

        result = self.client.post(self.login_url, payload)

        self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("username", result.data)
        self.assertIn("password", result.data)
        self.assertEqual(result.data["username"][0], "This field may not be blank.")
        self.assertEqual(result.data["password"][0], "This field may not be blank.")