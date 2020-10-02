from uuid import uuid4

from django.contrib.auth.models import User
from django.test import TestCase

from catalog.models import Product
from scrapping import NUTELLA
from search.views import ProductAutocomplete


class TestPattern(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='test1',
            password='test1@1234'
        )

        self.client.login(username='test1', password='test1@1234')

        self.product_1 = Product(
                id=uuid4(),
                product_name_fr='produit bon',
                nutrition_grade_fr='A',
                categories_tags=['Pâte à tartiner']
        )
        self.product_2 = Product(**NUTELLA)

        self.product_1.save()
        self.product_2.save()


class TestFavorite(TestPattern):
    def test_save_favorite(self):
        qs = ProductAutocomplete().get_queryset()


    def test_delete_favorite(self):
        ...

    def test_save_favorite_wrong_nutriscore(self):
        ...


class TestSearchProduct(TestPattern):
    def test_find_product_better_nutriscore(self):
        ...