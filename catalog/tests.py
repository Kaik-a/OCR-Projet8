"""Tests on catalog module"""
import ast
from django.contrib.auth.models import User
from django.test import TestCase
import uuid

import catalog.populate as populate
from .models import Category, Favorite, Product
from scrapping import NUTELLA, ID_PRODUCT


# Create your tests here.

class TestCategories(TestCase):
    """Tests on categories."""
    def test_populate_category(self):
        """Test populate categories"""
        categories = [
            {'name': 'boissons', 'url': 'http://boissons.con'},
            {'name': 'snacks', 'url': 'http://snack.com'}
        ]

        populate.populate_categories(categories)

        assert len(Category.objects.all()) == 2

    def test_add_category_db(self):
        """Test adding category to catalog."""
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
    def test_populate_product(self):
        """Test populate db with product"""
        populate.populate_product([NUTELLA])

        assert Product.objects.get(brands='Ferrero').product_name_fr == 'Nutella'

        # Test that only the 100g attributes are exported to db
        for nutriment in ast.literal_eval(Product.objects.get(
                brands='Ferrero'
        ).nutriments):
            for key in nutriment:
                assert key.find('100g') != -1

    def test_add_product_db(self):
        """Test adding product to db."""
        product = Product(
            **NUTELLA
        )

        # save product on db
        product.save()

        # verify Product saved on db
        assert len(Product.objects.all()) == 1

        # retrieve product name in the db
        assert Product.objects.get(
            id=ID_PRODUCT
        ).product_name_fr == 'Nutella'


class TestFavorite(TestCase):
    def test_add_favorite_db(self):
        """Add a new favorite to db"""
        product_1 = Product(
                product_name_fr='produit bon',
                nutrition_grade_fr='A'
            )
        product_2 = Product(**NUTELLA)

        product_1.save()
        product_2.save()

        user = User(username='Utilisateur')
        user.save()

        populate.save_favorite(
            product_1,
            product_2,
            user
        )

        assert len(Favorite.objects.all()) == 1
