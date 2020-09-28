from django.core.management.base import BaseCommand, CommandError

from catalog.models import Category, Product, Favorite


class Command(BaseCommand):
    help = "Empty the database"

    def add_arguments(self, parser):
        parser.add_argument('emptydb', nargs='+', type=bool)

    def handle(self, *args, **options):
        if options['emptydb']:
            try:
                Category.objects.all().delete()
                Product.objects.all().delete()
                Favorite.objects.all().delete()
            except Exception as e:
                raise CommandError(f"Error while emptying database - {e}")
