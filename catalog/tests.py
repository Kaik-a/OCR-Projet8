"""Tests on catalog module"""
import ast
import uuid
from io import StringIO

from django.contrib.auth.models import User
from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

import catalog.populate as populate
from scrapping import ID_PRODUCT, NUTELLA

from .models import Category, Favorite, Product


class TestCategories(TestCase):
    """Tests on categories."""

    def test_populate_category(self):
        """Test populate categories"""
        categories = [
            {"name": "boissons", "url": "http://boissons.con"},
            {"name": "snacks", "url": "http://snack.com"},
        ]

        populate.populate_categories(categories)

        assert len(Category.objects.all()) == 2

    def test_add_category_db(self):
        """Test adding category to catalog."""
        id_category = uuid.uuid4()
        category = Category(
            id_category=id_category,
            name="Charcuteries",
            url="https://fr.openfoodfacts.org/categorie/charcuteries",
        )

        # save category to db
        category.save()

        # verify Category saved on db
        assert len(Category.objects.all()) == 1

        # retrieve category name in the db
        assert Category.objects.get(id_category=id_category).name == "Charcuteries"


class TestProduct(TestCase):
    """Tests on products."""

    def test_populate_product(self):
        """Test populate db with product"""
        nutella = dict(NUTELLA)
        nutella["nutriments"] = {
            "sugars_100g": 12.8,
            "fat_100g": 8.97,
            "saturated-fat_100g": 1.28,
            "salt_100g": 2.05,
        }
        populate.populate_product([nutella])

        assert Product.objects.get(brands="Ferrero").product_name_fr == "Nutella"

        # Test that only the 100g attributes are exported to db
        for nutriment in ast.literal_eval(
            Product.objects.get(brands="Ferrero").nutriments
        ):
            for key in nutriment:
                assert key.find("100g") != -1

    def test_add_product_db(self):
        """Test adding product to db."""
        product = Product(**NUTELLA)

        # save product on db
        product.save()

        # verify Product saved on db
        assert len(Product.objects.all()) == 1

        # retrieve product name in the db
        assert Product.objects.get(id=ID_PRODUCT).product_name_fr == "Nutella"


class TestFavorite(TestCase):
    """Test on favorite"""

    def test_add_favorite_db(self):
        """Add a new favorite to db"""
        product_1 = Product(product_name_fr="produit bon", nutrition_grade_fr="A")
        product_2 = Product(**NUTELLA)

        product_1.save()
        product_2.save()

        user = User(username="Utilisateur")
        user.save()

        populate.save_favorite(product_1, product_2, user)

        assert len(Favorite.objects.all()) == 1


class TestViews(TestCase):
    """Test on catalog's views"""

    def setUp(self) -> None:
        """Tests configuration."""
        self.test_user = User.objects.create_user(
            "test_user", "test_user@test.com", "test_password"
        )
        self.client.login(username="test_user", password="test_password")
        self.product = Product(**NUTELLA)
        self.product.save()

    def test_aliment(self):
        """Load aliment"""
        url = reverse(
            "catalog:aliment", kwargs={"product_id": Product.objects.all()[0].id}
        )

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_favorites(self):
        """Load favorites"""
        url = reverse("catalog:favorites", kwargs={"user": self.test_user.id})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_results(self):
        """Load results"""
        url = reverse("catalog:results", kwargs={"base_product": str(self.product.id)})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)


class DjangoAdminCommandTest(TestCase):
    """Test django commands."""

    def test_empty_database(self):
        """Verify if database correctly emptied"""
        out = StringIO()
        call_command("empty_database", True, stdout=out)
        self.assertIn("Database correctly emptied", out.getvalue())
