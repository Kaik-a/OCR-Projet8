from uuid import uuid4

ID_PRODUCT = uuid4()

GIVEN_CATEGORIES = [
    'Fromages',
    'Snacks',
    'Boissons',
    'Charcuteries',
    'Desserts'
]
OPENFOODFACT_URL = 'https://fr.openfoodfacts.org/'
CATEGORIES_JSON = OPENFOODFACT_URL + 'categories'  # url of categories
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
NUTELLA = {
    'id': ID_PRODUCT,
    'brands': 'Ferrero',
    'category_tags': 'Pâte à tartiner',
    'nutrition_grade_fr': 'F',
    'nutriments': {
         "sodium": "0.629",
         "sugars": 10,
         "carbohydrates_unit": "g",
         "fat_unit": "g",
         "proteins_unit": "g",
         "nutrition-score-fr_100g": 15,
         "fat": 7,
         "proteins_serving": 7,
         "sodium_serving": 0.629,
         "salt": 1.59766,
         "proteins": 7,
         "nutrition-score-fr": 15,
         "sugars_unit": "g",
         "fat_serving": 7,
         "sodium_unit": "mg",
         "sugars_100g": "12.8",
         "saturated-fat_unit": "g",
         "sodium_100g": 0.806,
         "saturated-fat_serving": 1,
         "fiber_unit": "g",
         "energy": 1297,
         "energy_unit": "kcal",
         "sugars_serving": 10,
         "carbohydrates_100g": 70.5,
         "nutrition-score-uk": 15,
         "proteins_100g": 8.97,
         "fiber_serving": 0,
         "carbohydrates_serving": 55,
         "energy_serving": 1297,
         "fat_100g": "8.97",
         "saturated-fat_100g": "1.28",
         "nutrition-score-uk_100g": 15,
         "fiber": 0,
         "salt_serving": 1.59766,
         "salt_100g": "2.05",
         "carbohydrates": 55,
         "fiber_100g": 0,
         "energy_100g": 1660,
         "saturated-fat": 1
    },
    'product_name_fr': 'Nutella',
    'url_img': 'http://nutella-images.fr',
    'url': 'http://off-nutella-link.fr'
}