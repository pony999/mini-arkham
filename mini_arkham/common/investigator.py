class Investigator:
    def __init__(self, sanity: int, stamina: int, fight: int, will: int):
        self.sanity = sanity
        self.stamina = stamina
        self.fight = fight
        self.will = will
        self.insane = False
        self.unconscious = False

    def __str__(self):
        return f"INVESTIGATOR STATS:\n" \
               f">> sanity:  {self.sanity}\n" \
               f">> stamina: {self.stamina}\n" \
               f">> will:    {self.will}\n" \
               f">> fight:   {self.fight}\n" \
               f"#############"
