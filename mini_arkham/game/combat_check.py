from mini_arkham.common.investigator import Investigator
from mini_arkham.common.monster import Monster

from mini_arkham.game import dice


def combat_check(investigator: Investigator, monster: Monster) -> bool:
    """Skill check using the investigator's Fight value.
    The value is modified by the monster's combat rating.
    The difficulty of this check is equal to the monster's toughness."""

    test_difficulty = monster.toughness
    test_attempts = investigator.fight - monster.combat_rating

    user_introduction = " ".join(["Investigator attacks the monster...",
                                  f"\nInvestigator's fight ({investigator.fight}),",
                                  f"against monster's combat rating ({monster.combat_rating}), gives a",
                                  f"{test_attempts} dice" if test_attempts > 1 else "single die",
                                  f"throw."])
    print(user_introduction)

    success_quantity = sum(
        dice.roll() for _ in range(test_attempts)
    )
    print(f'Success count (number of attempts): {success_quantity} ({test_attempts}). Required {test_difficulty}.')

    if success_quantity < test_difficulty:
        return False
    else:
        return True


def combat_damage(investigator: Investigator, monster: Monster) -> None:
    investigator.reduce("stamina", monster.combat_damage)
    print(f'Monster deals physical damage to the investigator. Remaining stamina: {investigator.stamina}')

    if investigator.stamina == 0:
        investigator.unconscious = True
