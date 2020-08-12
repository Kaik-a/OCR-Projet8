"""Tests on categories"""
import requests
import unittest.mock as mock
import uuid

from django.test import TestCase

from . import GIVEN_CATEGORIES
from .categories import get_categories
from .products import get_products
from database.models import Category, Product


class TestCategories(TestCase):
    """Tests on categories."""
    def test_get_categories(self):
        """Tests to retrieve categories from oof."""
        requests.get = mock.MagicMock(return_value=requests.Response())
        patch = mock.patch(
            'requests.Response.json',
            new=mock.Mock(
                return_value={
                    'count': 12345,
                    'tags': [
                        {
                            'id': 'en:plant-based-foods-and-beverages',
                            'known': 1,
                            'name': 'Aliments et boissons à base de végétaux',
                            'url': 'https://fr.openfoodfacts.org/categorie'
                                   '/aliments-et-boissons-a-base-de-vegetaux',
                            'products': 88698
                        },
                        {
                            'url': 'https://fr.openfoodfacts.org/categorie'
                                   '/charcuteries',
                            'products': 18748,
                            'known': 1,
                            'id': 'en:prepared-meats',
                            'name': 'Charcuteries'
                        }
                    ]
                }
            )
        )

        patch.start()

        assert len(get_categories()) == 1

        patch.stop()

    def test_add_category_db(self):
        """Test adding category to database."""
        id_category = uuid.uuid4()
        category = Category(
            id_category=id_category,
            name='Charcuteries',
            url='https://fr.openfoodfacts.org/categorie/charcuteries'
        )

        # save category to db
        category.save()

        # verify Category saved on db
        assert len(Category.objects.all()) == 1

        # retrieve category name in the db
        assert Category.objects.get(
            id_category=id_category
        ).name == 'Charcuteries'


class TestProduct(TestCase):
    """Tests on products."""
    def test_get_products(self):
        """Test getting a product from OpenFoodFacts."""
        id_product_1 = uuid.uuid4()
        id_product_2 = uuid.uuid4()

        requests.get = mock.MagicMock(return_value=requests.Response())

        patch = mock.patch(
            'requests.Response.json',
            new=mock.Mock(
                return_value={
                    'products': [
                        {
                            'id': id_product_1,
                            'brands': 'Lactel',
                            'category_tags': 'Boissons',
                            'nutrition_grade': 'B',
                            'product_name_fr': 'Lait',
                            'url_img': 'http://lactel-images.fr',
                            'url': 'http://off-lactel.fr'
                        },
                        {
                            'id': id_product_2,
                            'brands': 'Candia',
                            'category_tags': 'Boissons',
                            'nutrition_grade': 'A',
                            'product_name_fr': 'Lait',
                            'url_img': 'http://candia-images.fr',
                            'url': 'http://off-candia.fr'
                        }
                    ]
                }
            )
        )

        patch.start()

        assert len(get_products(['Boissons'])) == 2

        patch.stop()

    def test_add_product_db(self):
        """Test adding product to db."""
        id_product = uuid.uuid4()
        product = Product(
            id=id_product,
            brands='Ferrero',
            category_tags='Pâte à tartiner',
            nutrution_grade='F',
            product_name_fr='Nutella',
            url_img='http://nutella-images.fr',
            url='http://off-nutella-link.fr'
        )

        # save product on db
        product.save()

        # verify Product saved on db
        assert len(Product.objects.all()) == 1

        # retrieve product name in the db
        assert Product.objects.get(
            id=id_product
        ).product_name_fr == 'Nutella'

