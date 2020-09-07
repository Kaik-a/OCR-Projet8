from django.core.management.base import BaseCommand, CommandError

from catalog.models import Category
from catalog.populate import populate_categories, populate_product
from scrapping.categories import get_categories
from scrapping.products import get_products


class Command(BaseCommand):
    help = "Populates the database"

    def add_arguments(self, parser):
        parser.add_argument('populate', nargs='+', type=bool)

    def handle(self, *args, **options):
        if options['populate']:

            try:
                categories = get_categories()
            except Exception as e:
                raise CommandError(f"Error while scrapping categories- {e}")

            try:
                populate_categories(categories)
            except Exception as e:
                raise CommandError(f"Error while populating categories- {e}")

            try:
                products = get_products(
                    [category.name for category in Category.objects.all()]
                )
            except Exception as e:
                raise CommandError(f"Error while scrapping products - {e}")

            try:
                populate_product(products)
            except Exception as e:
                raise CommandError(f"Error while populating products - {e}")

