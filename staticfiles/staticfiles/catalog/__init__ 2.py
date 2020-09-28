NUTRISCORE = {
    'A': 'Ⓐ',
    'B': 'Ⓑ',
    'C': 'Ⓒ',
    'D': 'Ⓓ',
    'E': 'Ⓔ',
}

# max value for nutriments for being low and moderate
# values are divided by two for drinks
NUTRIMENTS = {
    'saturated-fat': {
        'value': {'low': 1.5, 'moderate': 5},
        'traduction': 'Acides gras saturés'
    },
    'fat': {'value': {
        'low': 3, 'moderate': 20},
        'traduction': 'Matières grasses / Lipides'
    },
    'sugars': {'value': {'low': 5, 'moderate': 12.5}, 'traduction': 'Sucres'},
    'salt': {'value': {'low': 0.3, 'moderate': 1.5}, 'traduction': 'Sels'}
}