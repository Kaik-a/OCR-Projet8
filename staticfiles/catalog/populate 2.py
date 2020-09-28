"""Insert products in catalog"""
from datetime import datetime
from typing import List, Dict
from uuid import uuid4

from django.contrib.auth.models import User
from django.db import IntegrityError

from . import NUTRIMENTS
from .models import Category, Favorite, Product


def populate_product(products: List) -> None:
    """Insert a list of products in catalog.

    :param list products: List of products to insert in db.
    :rtype: None
    """
    list_product: List[Product] = []
    for product in products:
        try:
            list_product.append(
                Product(
                    uuid4(),
                    product.get('brands'),
                    product.get('categories_tags'),
                    [{key: value} for key, value in product.get('nutriments').items()
                     if key.find('100g') != -1 and key[:-5] in NUTRIMENTS.keys()],
                    product.get('nutrition_grade_fr'),
                    product.get('product_name_fr'),
                    product.get('image_url'),
                    product.get('url'),
                )
            )
        except TypeError:
            continue

    for product_object in list_product:
        if product_object.brands and product_object.categories_tags \
            and product_object.nutriments and product_object.nutrition_grade_fr \
            and product_object.product_name_fr and product_object.image_url \
                and product_object.url:
            try:
                product_object.save()
            except IntegrityError:
                continue


def populate_categories(categories: List) -> None:
    """Insert a list of categories in catalog.

    :param list categories: List of categories to insert in db.
    :rtype: None
    """
    try:
        Category.objects.bulk_create([Category(**{
            'id_category': uuid4(),
            'name': category['name'],
            'url': category['url']
            }) for category in categories])
    except TypeError as e:
        raise e


def save_favorite(
        product_to_save: Product,
        product_to_replace: Product,
        user: User) -> None:
    """Save a product as a favorite.

    :param Product product_to_save: product to save as a favorite.
    :param Product product_to_replace: product to replace.
    :param User user: user who made the comparaison
    :rtype: None
    """
    try:
        if product_to_save.nutrition_grade_fr < product_to_replace.nutrition_grade_fr:
            Favorite(
                substitute=product_to_save,
                substitued=product_to_replace,
                user=user,
                date=datetime.now()
            ).save()
    except Exception as e:
        print(e)
