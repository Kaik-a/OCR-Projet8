GIVEN_CATEGORIES = [
    'Fromages',
    'Snacks',
    'Boissons',
    'Charcuteries',
    'Desserts'
]
OPENFOODFACT_URL = 'https://fr.openfoodfacts.org/'
CATEGORIES_JSON = OPENFOODFACT_URL + 'categories.json'  # url of categories
SEARCH_URL = OPENFOODFACT_URL + 'cgi/search.pl'
BASE_SEARCH_PARAMS = {
    'action': 'process',
    'tagtype_0': 'categories',
    'tagcontains_0': 'contains',
    'limit': 5000,
    'tag_0': 'test',
    'page_size': 1000,
    'sort_by': 'unique_scans_n',
    'json': 1,
}