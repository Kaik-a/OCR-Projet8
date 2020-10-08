"""Tests on scrapping methods"""
import unittest.mock as mock
import uuid

import requests
from django.test import TestCase

from . import NUTELLA
from .categories import get_categories
from .products import get_products


class TestCategories(TestCase):
    """Tests on categories."""

    def test_get_categories(self):
        """Tests to retrieve categories from oof."""
        requests.get = mock.MagicMock(return_value=requests.Response())
        patch = mock.patch(
            "requests.Response.json",
            new=mock.Mock(
                return_value={
                    "count": 12345,
                    "tags": [
                        {
                            "id": "en:plant-based-foods-and-beverages",
                            "known": 1,
                            "name": "Aliments et boissons à base de végétaux",
                            "url": "https://fr.openfoodfacts.org/categorie"
                            "/aliments-et-boissons-a-base-de-vegetaux",
                            "products": 88698,
                        },
                        {
                            "url": "https://fr.openfoodfacts.org/categorie"
                            "/charcuteries",
                            "products": 18748,
                            "known": 1,
                            "id": "en:prepared-meats",
                            "name": "Charcuteries",
                        },
                    ],
                }
            ),
        )

        patch.start()

        assert len(get_categories()) == 1

        patch.stop()


class TestProduct(TestCase):
    """Tests on products."""

    def test_get_products(self):
        """Test getting a product from OpenFoodFacts."""
        id_product_2 = uuid.uuid4()

        requests.get = mock.MagicMock(return_value=requests.Response())

        patch = mock.patch(
            "requests.Response.json",
            new=mock.Mock(
                return_value={
                    "products": [
                        NUTELLA,
                        {
                            "id": id_product_2,
                            "brands": "Candia",
                            "category_tags": "Boissons",
                            "nutrition_grade_fr": "A",
                            "product_name_fr": "Lait",
                            "url_img": "http://candia-images.fr",
                            "url": "http://off-candia.fr",
                        },
                    ]
                }
            ),
        )

        patch.start()

        assert len(get_products(["Boissons"])) == 2

        patch.stop()
