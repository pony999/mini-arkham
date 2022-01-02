from mini_arkham.common.investigator import Investigator
from mini_arkham.common.monster import Monster

from mini_arkham.game.horror_check import horror_check, horror_damage
from mini_arkham.game.combat_check import combat_check, combat_damage


def combat(investigator: Investigator, monster: Monster) -> bool:
    """During any duel between investigator and monster the investigator starts with a single horror check.
    Successful check has on effect while failed test leads to sanity damage, which might lead to insanity.

    The duel then follows up with a physical combat when investigator tries to kill the monster with combat check.
    In case the check is successful the investigator wins the duel.
    Failed test result leads to monster attack and stamina damage to investigator, which might lead to unconsciousness.

    Combat test is repeated until either is defeated.
    :returns(bool): True if investigator wins and False if defeated

    TODO: introduce Evade check"""

    print("\nYour investigator runs into a monster...")
    input("Press enter to continue...")

    if not horror_check(investigator, monster):
        horror_damage(investigator, monster)

    if investigator.insane:
        return False

    input("\nPress enter to continue...")

    while True:
        if combat_check(investigator, monster):
            print("Monster is defeated.")
            return True
        else:
            combat_damage(investigator, monster)

            if investigator.unconscious:
                return False

        print("\nThe fight continues...")
        input("Press enter to continue...")

