from .factories import UserFactory
from django.test import TestCase


class TestAuth(TestCase):
    def test_login(self):
        self.user = UserFactory.with_password("secret123")

        resp = self.client.post(
            "/api/v1/auth/login/",
            {"username": "testuser", "email": self.user.email, "password": "secret123"},
            content_type="application/json",
        )

        self.assertEqual(resp.status_code, 200)
        self.assertTrue("key" in resp.json())

    def test_signup(self):
        resp = self.client.post(
            "/api/v1/auth/register/",
            {
                "username": "testuser",
                "email": "test@example.com",
                "password1": "S3cr3t?N0tR34lly",
                "password2": "S3cr3t?N0tR34lly",
            },
            content_type="application/json",
        )

        self.assertEqual(resp.status_code, 201)
        self.assertTrue("key" in resp.json())
