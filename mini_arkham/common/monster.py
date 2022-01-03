class Monster:
    def __init__(self, awareness: int, horror_rating: int, horror_damage: int,
                 toughness: int, combat_rating: int, combat_damage: int):
        self.awareness = awareness
        self.horror_rating = horror_rating
        self.horror_damage = horror_damage
        self.toughness = toughness
        self.combat_rating = combat_rating
        self.combat_damage = combat_damage

    def __str__(self):
        return f"MONSTER DETAILS:\n" \
               f">> awareness: {self.awareness}\n" \
               f">> horror rating: {self.horror_rating}\n" \
               f">> horror damage: {self.horror_damage}\n" \
               f">> combat rating: {self.combat_rating}\n" \
               f">> combat damage: {self.combat_damage}\n" \
               f">> toughness: {self.toughness}"
