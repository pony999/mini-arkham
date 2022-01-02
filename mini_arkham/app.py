from common.investigator import Investigator
from common.monster import Monster
from game import combat

investigator_stats = {'sanity': 5, 'stamina': 5, 'fight': 4, 'will': 3}
player = Investigator(**investigator_stats)


monster_stats = {'horror_rating': 0, 'horror_damage': 3, 'combat_rating': 3, 'combat_damage': 3,
                 'awareness': 3, 'toughness': 1}
monster = Monster(**monster_stats)

print(">>> SINGLE GAME SIMULATION <<<")
print("#######################")
print(player)
print(monster)
print(combat.combat(player, monster))
