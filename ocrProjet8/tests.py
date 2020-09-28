from django.test import TestCase
from django.urls import reverse


class TestProject(TestCase):
    def test_home(self):
        url = reverse(
            'home'
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_contact(self):
        url = reverse(
            'contact'
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_mention(self):
        url = reverse(
            'notice'
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
