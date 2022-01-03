from mini_arkham.common.attributes import Attribute, Stamina, Sanity


class Investigator:
    def __init__(self, stamina: int, sanity: int, fight: int, will: int):

        self.stamina = Stamina(stamina)
        self.sanity = Sanity(sanity)

        self.fight = fight
        self.will = will
        self.insane = False
        self.unconscious = False

    def reduce(self, name: str, amount: int) -> None:
        """Calls reduce method for Attribute type parameters"""
        attr = getattr(self, name)
        if isinstance(attr, Attribute):
            attr.reduce(amount)

    def restore(self, name: str, amount: int) -> None:
        """Calls restore method for Attribute type parameters"""
        attr = getattr(self, name)
        if isinstance(attr, Attribute):
            attr.restore(amount)

    def __str__(self):
        """Instance's string representation"""
        return f"INVESTIGATOR DETAILS:\n" \
               f">> {self.sanity}\n" \
               f">> {self.stamina}\n" \
               f">> will: {self.will}\n" \
               f">> fight: {self.fight}"
