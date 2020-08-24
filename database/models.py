import uuid

from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    """Class product.

    Args:
        id (UUID): Id of the product.
        brands (str): Brands where the product can be found.
        category_tags (str): Categories product belongs to.
        nutrition_grade_fr (str): A to E classification for healthfulness.
        product_name_fr (str): Name of the product in french.
        url_img (str): URL of the related image on OFF.
        url (str): URL on OFF
    """
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    brands = models.CharField(max_length=100)
    category_tags = models.CharField(max_length=500)
    nutriments = models.CharField(max_length=10000, default='')
    nutrition_grade_fr = models.CharField(max_length=1)
    product_name_fr = models.CharField(max_length=100)
    url_img = models.URLField()
    url = models.URLField()

    def __str__(self):
        return f"{self.product_name_fr}"


class Category(models.Model):
    """Class Category

    Args:
        id_category (UUID): Id of the category.
        name (str): Name of the category.
        url (URLField): URL of the category.
    """
    id_category = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return name


class Favorite(models.Model):
    """Class Favorite.

    Args:
        id_substitute (UUID): Id of the product found.
        id_substitued (UUID): Id of the product to find substitute for.
        date (DateTime): Date of the substitution.
    """
    substitute = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='fk_product_substitute'
    )

    substitued = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='fk_product_substitued'
    )
    date = models.DateTimeField()

    user = models.ForeignKey(
        User,
        default=None,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.id_substitued} a été remplacé par {self.id_substitute}"
