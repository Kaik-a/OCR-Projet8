from ast import literal_eval
from django.shortcuts import render, redirect
from typing import List

from django.urls import reverse

from catalog.models import Product
from search.forms import SearchForm


def home(request):
    if request.method == "POST":
        form: SearchForm = SearchForm(request.POST)

        if form.is_valid():
            base_product: Product = form.cleaned_data["produit"]

            return redirect(
                reverse("catalog:results", kwargs={'base_product': base_product.id})
            )
    else:
        form: SearchForm = SearchForm()
    return render(request, 'home.html', {'form': form})


def legal_notice(request):
    return render(request, 'notice.html')


def contact(request):
    return render(request, 'contact.html')
