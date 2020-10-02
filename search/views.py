from dal import autocomplete

from catalog.models import Product


class ProductAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        query_set = Product.objects.all()

        if self.q:
            query_set = query_set.filter(product_name_fr__istartswith=self.q)

        return query_set.order_by('product_name_fr')
