from datetime import datetime
from importlib import import_module
from unittest.mock import patch
from uuid import uuid4

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase, RequestFactory
from django.urls import reverse


from accounts.views import get_user_info, subscribe
from catalog.models import Product, Favorite


class TestUnauthenticated(TestCase):
    product_1 = Product(
        id=uuid4(),
        product_name_fr='test_product_1'
    )

    product_2 = Product(
        id=uuid4(),
        product_name_fr='test_product_2'
    )

    def test_user_account_while_unauthenticated(self):
        """If no user is authenticated, you should not access user_account."""
        url = reverse('accounts:user_account')
        response = self.client.get(url)
        self.assertTemplateNotUsed(response, 'account/user_account.html')
        self.failUnlessEqual(response.status_code, 302)

    def test_favorites_while_unauthenticated(self):
        """If no user is authenticated, you should not access favorites."""
        url = reverse('catalog:favorites', kwargs={'user': 'test'})
        response = self.client.get(url)
        self.assertTemplateNotUsed(response, 'catalog/favorites')
        self.failUnlessEqual(response.status_code, 302)

    def test_sign_out_unauthenticated(self):
        """If no user is authenticated, you should not be able to logout."""
        url = reverse('accounts:logout')
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 302)

    def test_save_unautenticated(self):
        """If no user is authenticated, you should not be able to save products."""
        url = reverse(
            'catalog:save',
            kwargs={
                'base_product': self.product_1.id,
                'substitute_product': self.product_2.id
            }
        )
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 302)

    def test_delete_favorite_unauthenticatedt(self):
        """If no user is authenticated, you should not be able to delete saved
        products."""
        url = reverse(
            'catalog:delete_favorite',
            kwargs={
                'product_id': self.product_1.id
            }
        )
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 302)


class TestAuthenticated(TestCase):
    product_1 = Product(
        id=uuid4(),
        product_name_fr='test_product_1'
    )

    product_2 = Product(
        id=uuid4(),
        product_name_fr='test_product_2'
    )

    def setUp(self) -> None:
        self.test_user = User.objects.create_user(
            'test_user',
            'test_user@test.com',
            'test_password'
        )
        self.client.login(
            username='test_user',
            password='test_password'
        )

        favorite = Favorite(
            substitued=self.product_1,
            substitute=self.product_2,
            user=User.objects.get(username='test_user'),
            date=datetime.now()
        )

        self.product_1.save()
        self.product_2.save()
        favorite.save()

    def test_user_account_while_authenticated(self):
        """If user is authenticated, you should access user_account."""
        url = reverse('accounts:user_account')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'user_account.html')
        self.assertEqual(response.status_code, 200)

    def test_favorites_while_authenticated(self):
        """If user is authenticated, you should access favorites."""
        user_id = User.objects.get(username='test_user').id
        url = reverse('catalog:favorites', kwargs={'user': user_id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'favorites.html')
        self.assertEqual(response.status_code, 200)

    def test_sign_out_authenticated(self):
        """If user is authenticated, you should be able to logout."""
        url = reverse('accounts:logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_save_autenticated(self):
        """If user is authenticated, you should be able to save products."""
        url = reverse(
            'catalog:save',
            kwargs={
                'base_product': self.product_1.id,
                'substitute_product': self.product_2.id
            }
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_delete_favorite_authenticated(self):
        """If user is authenticated, you should be able to delete saved
        products."""
        url = reverse(
            'catalog:delete_favorite',
            kwargs={
                'product_id': self.product_2.id
            }
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)




