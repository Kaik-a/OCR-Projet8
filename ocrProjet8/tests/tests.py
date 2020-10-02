from django.test import TestCase
from django.urls import reverse

from ocrProjet8.templatetags.navbar_search import navbar_search


class TestProject(TestCase):
    """Tests on ocrProjet views."""
    def test_home(self):
        """Load home"""
        url = reverse(
            'home'
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_contact(self):
        """Load contact"""
        url = reverse(
            'contact'
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_notice(self):
        """Load notice"""
        url = reverse(
            'notice'
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_navbar_search(self):
        ns = navbar_search(None, None)

        assert ns.form.fields['produit']

        self.assertEqual(ns.form.is_valid(), False)

