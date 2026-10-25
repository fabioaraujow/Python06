import alchemy.grimoire


def validate_ingredients(ingredients: str) -> str:
    ingredients_list = alchemy.grimoire.allowed()
    for current in ingredients_list:
        if current in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
