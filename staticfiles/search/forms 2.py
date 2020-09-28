from dal import autocomplete
from django import forms

from catalog.models import Product


class SearchForm(forms.ModelForm):
    produit = forms.ModelChoiceField(
        empty_label='Produit',
        queryset=Product.objects.all(),
        widget=autocomplete.ModelSelect2(url='product-autocomplete')
    )

    class Meta:
        model = Product
        fields = ()
