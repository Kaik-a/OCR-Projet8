"""Insert products in database"""
from typing import List
from uuid import uuid4

from .models import Category, Product


def populate_product(products: List) -> None:
    """Insert a list of products in database.

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
                    product.get('category_tags'),
                    [{key: value} for key, value in product.get('nutriments').items()
                     if key.find('100g') != -1],
                    product.get('nutrition_grade_fr'),
                    product.get('product_name_fr'),
                    product.get('url_img'),
                    product.get('url'),
                )
            )
        except TypeError:
            continue

    for product_object in list_product:
        if product_object.brands and product_object.category_tags \
            and product_object.nutriments and product_object.nutrition_grade_fr \
            and product_object.product_name_fr and product_object.url_img \
                and product_object.url:
            product_object.save()


def populate_categories(categories: List) -> None:
    """Insert a list of categories in database.

    :param list categories: List of categories to insert in db.
    :rtype: None
    """
    for category in categories:
        try:
            Category(
                uuid4(),
                category['name'],
                category['url']
            ).save()
        except TypeError:
            continue
