from mini_arkham.common.investigator import Investigator
from mini_arkham.common.monster import Monster

from mini_arkham.game import dice


def horror_check(investigator: Investigator, monster: Monster):
    """Skill check using the investigator's Will value.
    The value is modified by the monster's horror rating.
    The difficulty of this check is always 1 unless the monster has a special ability that states otherwise."""

    test_difficulty = 1
    test_attempts = investigator.will - monster.horror_rating

    user_introduction = " ".join(["The alien nature of the mythos threatens to overwhelm the investigator's mind...",
                                  f"\nInvestigator's will ({investigator.will}),",
                                  f"against monster's horror rating ({monster.horror_rating}), gives a",
                                  f"{test_attempts} dice" if test_attempts > 1 else "single die",
                                  f"throw."])
    print(user_introduction)

    success_quantity = sum(
        dice.roll() for _ in range(test_attempts)
    )
    print(f'Success count (number of attempts): {success_quantity} ({test_attempts}). Required {test_difficulty}.')

    if success_quantity < test_difficulty:
        print("Fails horror check...")
        return False
    else:
        print("Investigator passes the check, nothing happens.")
        return True


def horror_damage(investigator: Investigator, monster: Monster) -> None:
    """Investigator ming gets overwhelmed by a monster and looses sanity equal to monsters horror_damage"""
    investigator.reduce("sanity", monster.horror_damage)
