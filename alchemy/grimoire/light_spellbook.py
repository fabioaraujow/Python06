import alchemy.grimoire


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    validated = alchemy.grimoire.validate_ingredients(ingredients)
    if "INVALID" not in validated:
        return f"Spell recorded: {spell_name} ({validated})"
    return f"Spell not recorded: {spell_name} ({validated})"
