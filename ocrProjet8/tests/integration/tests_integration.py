"""Integrations tests"""
from datetime import datetime
from uuid import uuid4

from django.contrib.auth.models import User
from django.test import TestCase

from catalog.models import Favorite, Product
from scrapping import NUTELLA
from search.views import ProductAutocomplete


class TestPattern(TestCase):
    """Global set up"""

    def setUp(self) -> None:
        """Environment for tests"""
        self.user = User.objects.create_user(username="test1", password="test1@1234")

        self.client.login(username="test1", password="test1@1234")

        self.product_1 = Product(
            id=uuid4(),
            product_name_fr="produit bon",
            nutrition_grade_fr="A",
            categories_tags=["Pâte à tartiner"],
        )
        self.product_2 = Product(**NUTELLA)

        self.product_1.save()
        self.product_2.save()


class TestFavorite(TestPattern):
    """Test on Favorites"""

    def test_save_favorite(self):
        """Try to save a Favorite"""
        query_set = ProductAutocomplete().get_queryset()

        Favorite(
            substitute=query_set[0],
            substitued=query_set[1],
            user=self.user,
            date=datetime.now(),
        ).save()

        self.assertEqual(len(Favorite.objects.all().filter(user=self.user)), 1)

    def test_delete_favorite(self):
        """Try to delete a Favorite"""
        query_set = ProductAutocomplete().get_queryset()

        Favorite(
            substitute=query_set[0],
            substitued=query_set[1],
            user=self.user,
            date=datetime.now(),
        ).save()

        self.assertEqual(len(Favorite.objects.all().filter(user=self.user)), 1)

        Favorite.objects.get(substitute=query_set[0]).delete()

        self.assertEqual(len(Favorite.objects.all().filter(user=self.user)), 0)
