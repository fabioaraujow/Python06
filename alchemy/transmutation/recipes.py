from ..potions import strength_potion
from elements import create_fire
import alchemy


def lead_to_gold() -> str:
    return ("Recipe transmuting Lead to Gold: "
            f"brew '{alchemy.create_air()}' and "
            f"'{strength_potion()}' "
            f"mixed with '{create_fire()}'")
