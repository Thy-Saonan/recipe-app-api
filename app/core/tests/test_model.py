from django.test import TestCase

from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successfull"""
        email = "saonan.thy@kit.edu.kh"
        password = "Testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalized(self):
        """Test the email for new user is normalize"""
        email = "saonan@GMAIL.COM"
        user = get_user_model().objects.create_user(
            email=email,
            password="test123"
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_valid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password="pass123"
            )

    def test_create_new_superuser(self):
        """Test creating superuser"""
        user = get_user_model().objects.create_superuser(
            'test@cambo.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
