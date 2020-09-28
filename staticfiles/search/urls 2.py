from django.urls import path

from . import views
from .views import ProductAutocomplete
from catalog.models import Product

urlpatterns = [
    path(
        'product-autocomplete/',
        ProductAutocomplete.as_view(model=Product),
        name='product-autocomplete'
    ),
]
