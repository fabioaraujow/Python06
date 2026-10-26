from alchemy.grimoire.dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    ingredients_list = dark_spell_allowed_ingredients()
    for current in ingredients_list:
        if current in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
