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
                    product['brands'],
                    product['category_tags'],
                    product['nutrition_grade'],
                    product['product_name_fr'],
                    product['image_url'],
                    product['url'],
                )
            )
        except TypeError:
            continue

    for product_object in list_product:
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
