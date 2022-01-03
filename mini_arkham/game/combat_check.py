from mini_arkham.common.investigator import Investigator
from mini_arkham.common.monster import Monster

from mini_arkham.game import dice


def combat_check(investigator: Investigator, monster: Monster) -> bool:
    """Skill check using the investigator's Fight value.
    The value is modified by the monster's combat rating.
    The difficulty of this check is equal to the monster's toughness."""

    test_difficulty = monster.toughness
    test_attempts = investigator.fight - monster.combat_rating

    print("Investigator attempt to fight the monster...")
    print(f'Fight: {investigator.fight}; combat_rating: {monster.combat_rating}')

    success_quantity = sum(
        dice.roll() for _ in range(test_attempts)
    )
    print(f'Success count (number of attempts): {success_quantity} ({test_attempts})')

    if success_quantity < test_difficulty:
        return False
    else:
        return True


def combat_damage(investigator: Investigator, monster: Monster) -> None:
    investigator.reduce("stamina", monster.combat_damage)
    print(f'Monster deals physical damage to the investigator. Remaining stamina: {investigator.stamina}')

    if investigator.stamina == 0:
        print("The investigator is knocked unconscious and no longer able to fight.")
        investigator.unconscious = True
