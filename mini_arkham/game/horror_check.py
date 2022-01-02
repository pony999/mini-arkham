from mini_arkham.common.investigator import Investigator
from mini_arkham.common.monster import Monster

from mini_arkham.game import dice


def horror_check(investigator: Investigator, monster: Monster):
    """Skill check using the investigator's Will value.
    The value is modified by the monster's horror rating.
    The difficulty of this check is always 1 unless the monster has a special ability that states otherwise."""

    test_difficulty = 1
    test_attempts = investigator.will - monster.horror_rating

    print("The alien nature of the mythos threatens to overwhelm the investigator's mind...")
    print(f'Investigator\'s will is: {investigator.will}; horror rating: {monster.horror_rating}')

    success_quantity = sum(
        dice.roll() for _ in range(test_attempts)
    )
    print(f'Success count (number of attempts): {success_quantity} ({test_attempts})')

    if success_quantity < test_difficulty:
        print("Investigator fails the horror check...")
        return False
    else:
        print("Investigator passes the check, nothing happens")
        return True


def horror_damage(investigator: Investigator, monster: Monster) -> None:
    investigator.sanity = max(investigator.sanity - monster.horror_damage, 0)
    print(f'Investigator takes mind damage. Remaining sanity: {investigator.sanity}')

    if investigator.sanity == 0:
        print("The investigator is driven temporarily insane and no longer able to fight.")
        investigator.insane = True
