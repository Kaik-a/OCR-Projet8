"""Define the toolbar search for all templates"""
from django.shortcuts import redirect, render
from django.urls import reverse

from catalog.models import Product
from search.forms import SearchForm


def toolbar_search(request):
    toolbar_form: SearchForm = SearchForm(request.POST)

    form_parameters = toolbar_form.fields['produit']

    form_parameters.label = ''
    form_parameters.required = False

    return {'toolbar_form': toolbar_form}
