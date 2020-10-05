"""Init for catalog"""

NUTRISCORE = {
    "A": ("Ⓐ", "#328F00"),
    "B": ("Ⓑ", "#54EA03"),
    "C": ("Ⓒ", "#FFDC00"),
    "D": ("Ⓓ", "#FF9B00"),
    "E": ("Ⓔ", "#FF2E00"),
}

# max value for nutriments for being low and moderate
# values are divided by two for drinks
NUTRIMENTS = {
    "saturated-fat": {
        "value": {"low": 1.5, "moderate": 5},
        "traduction": "Acides gras saturés",
    },
    "fat": {
        "value": {"low": 3, "moderate": 20},
        "traduction": "Matières grasses / Lipides",
    },
    "sugars": {"value": {"low": 5, "moderate": 12.5}, "traduction": "Sucres"},
    "salt": {"value": {"low": 0.3, "moderate": 1.5}, "traduction": "Sels"},
}
