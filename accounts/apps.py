"""Apps for accounts"""
from django.apps import AppConfig  # pylint: disable=import-error


class AuthenticationConfig(AppConfig):  # pylint: disable=too-few-public-methods
    """Config for accounts"""
    name = 'accounts'
