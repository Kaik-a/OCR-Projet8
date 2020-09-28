from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class TestAccount(TestCase):
    def test_user_account_while_unauthenticated(self):
        """IF no user is authenticated, you should not access user_account."""
        url = reverse('accounts:user_account')
        response = self.client.get(url)
        self.assertTemplateNotUsed(response, 'account/user_account.html')
        self.failUnlessEqual(response.status_code, 302)
