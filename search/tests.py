import ast

from django.test import TestCase


# Create your tests here.
from django.urls import reverse

from catalog.models import Product


class TestSearch(TestCase):
    def setUp(self) -> None:
        Product(product_name_fr='nutella').save()
        Product(product_name_fr='lait').save()
        Product(product_name_fr='fromage de chèvre').save()
        Product(product_name_fr='pain').save()

    def test_search(self):
        url = reverse(
            'product-autocomplete'
        )

        response = self.client.get(url)

        results = response.json()['results']

        assert results[0]['text'] == 'fromage de chèvre'
        assert results[1]['text'] == 'lait'
        assert results[2]['text'] == 'nutella'
        assert results[3]['text'] == 'pain'
