from alchemy.grimoire.dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validated = validate_ingredients(ingredients)
    if "INVALID" not in validated:
        return f"Spell recorded: {spell_name} ({validated})"
    return f"Spell not recorded: {spell_name} ({validated})"
