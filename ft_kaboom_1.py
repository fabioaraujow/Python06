#!/usr/bin/env python3
print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN EXCEPTION")
try:
    import alchemy.grimoire.dark_spellbook
    print(alchemy.grimoire.dark_spellbook.dark_spell_record(
        'Fantasy', 'frog'))
except ImportError as err:
    print(f"Import Error: {err}")
