from mini_arkham.common.investigator import Investigator
from mini_arkham.common.monster import Monster

from mini_arkham.game.horror_check import horror_check, horror_damage
from mini_arkham.game.combat_check import combat_check, combat_damage


def combat(investigator: Investigator, monster: Monster) -> bool:
    """During any duel between an investigator and a monster the investigator starts with a single horror check.
    Successful check has on effect, while failed test leads to sanity damage, which might lead to insanity.

    The duel then continues with a physical combat, during when the investigator attempts to kill the monster.
    He/she performs combat check and in case of success the investigator wins the duel.
    Failed test leads to a subsequent monster attack resulting in stamina reduction to investigator.
    If investigator's stamina reaches 0, he/she gets to unconscious and therefore defeated.

    Combat test is repeated until either is defeated.
    :returns(bool): True if investigator wins and False if defeated

    TODO: introduce Evade check prior to any of horror/combat checks"""

    print("\nYour investigator runs into a monster...")
    input("Press ENTER to continue...\n")

    if not horror_check(investigator, monster):
        horror_damage(investigator, monster)

    if investigator.insane:
        return False

    input("Press ENTER to continue...\n")

    while True:
        if combat_check(investigator, monster):
            print("Monster is defeated.")
            return True
        else:
            combat_damage(investigator, monster)

            if investigator.unconscious:
                print("The investigator is knocked unconscious and no longer able to fight.")
                return False

        print("\nThe fight continues...")
        input("Press ENTER to continue...")

