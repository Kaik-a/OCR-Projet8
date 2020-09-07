import ast
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from typing import List

from . import NUTRISCORE
from .models import Product


def aliment(request, product: Product):
    nutriments: List = ast.literal_eval(product.nutriments)
    return render(request, "aliment.html", {
        'product': product,
        'nutriments': nutriments
    })


@login_required
def favorites(request, products: List[Product]):
    return render(request, "favorites.html", {'products': products})


def results(request, products: List[Product]):
    return render(request, "results.html", {
        'products': products,
        'nutriscores': NUTRISCORE
    })
