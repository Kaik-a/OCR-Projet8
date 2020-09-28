import ast
import datetime
from typing import List
from uuid import UUID

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.shortcuts import render, redirect

from . import NUTRISCORE
from .models import Product, Favorite


def aliment(request, product_id):
    product = Product.objects.get(id=product_id)
    nutriments: List = ast.literal_eval(product.nutriments)
    return render(request, "aliment.html", {
        'product': product,
        'nutriments': nutriments
    })


@login_required
def favorites(request, user: str):
    products: List[Product] = [Product.objects.get(id=favorite.substitute.id)
                               for favorite in Favorite.objects.filter(user=user)]
    paginator = Paginator(products, 6)

    page = request.GET.get('page')

    page_obj = paginator.get_page(page)

    context = {'products': products, 'nutriscores': NUTRISCORE, 'page_obj': page_obj}

    return render(
        request,
        "favorites.html",
        context
    )


def results(request, base_product):
    base_product = Product.objects.get(id=base_product)
    categories: List = ast.literal_eval(base_product.categories_tags)
    nutrition_grade: str = base_product.nutrition_grade_fr
    products: List[Product] = []

    for category in categories:
        [products.append(product) for product in Product.objects.filter(
            categories_tags__contains=category,
            nutrition_grade_fr__cn=nutrition_grade
        )]

    products.sort(key=lambda x: x.nutrition_grade_fr)
    paginator = Paginator(products, 6)

    page = request.GET.get('page')

    page_obj = paginator.get_page(page)

    context = {
        'base_product': base_product,
        'products': products,
        'nutriscores': NUTRISCORE,
        'page_obj': page_obj
    }

    return render(request, "results.html", context)


@login_required
def save(request, base_product: UUID, substitute_product: UUID):
    user = request.user

    base = Product.objects.get(id=base_product)
    substitute = Product.objects.get(id=substitute_product)

    new_favorite: Favorite = Favorite(
        substitued=base,
        substitute=substitute,
        date=datetime.datetime.now(),
        user=user
    )

    try:
        new_favorite.save()
    except IntegrityError as e:
        messages.add_message(
            request,
            40,
            f"Le substitut {substitute.product_name_fr} n'a pas pu être enregistré "
            f"suite à l'erreur suivante: {e}"
        )
        return redirect("catalog:results", base_product=base_product)

    messages.add_message(
        request,
        25,
        f'Le produit {substitute.product_name_fr} a correctement été ajouté '
        f'à vos favoris'
    )
    return redirect("catalog:results", base_product=base_product)


@login_required
def delete_favorite(request, product_id: UUID):
    user = request.user

    to_delete = Favorite.objects.get(substitute=product_id, user=user)

    product_name = Product.objects.get(id=product_id).product_name_fr
    try:
        to_delete.delete()
    except IntegrityError as e:
        messages.add_message(
            request,
            40,
            f"Nous n'avons pas réussis à supprimer le produit "
            f"{product_name} pour la raison suivante: {e}"
        )

    messages.add_message(
        request,
        25,
        f'Le produit {product_name} est correctement supprimé de vos favoris'
    )
    return redirect("catalog:favorites", user=user.id)
