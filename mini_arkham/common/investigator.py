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
        """Calls reduce method for Sanity or Stamina type parameters"""
        attr = getattr(self, name)

        if isinstance(attr, Sanity):
            attr.reduce(amount)
            print(f'Investigator takes mind damage. Remaining sanity: {self.sanity}')
            self.is_going_insane()

        if isinstance(attr, Stamina):
            attr.reduce(amount)
            print(f'Investigator takes physical damage. Remaining stamina: {self.stamina}')
            self.is_going_unconscious()

    def restore(self, name: str, amount: int) -> None:
        """Calls restore method for Sanity or Stamina type parameters"""
        attr = getattr(self, name)

        if isinstance(attr, Sanity):
            attr.restore(amount)
            print(f'Investigator restores sanity. Current value: {self.sanity}')
            self.is_no_longer_insane()

        if isinstance(attr, Stamina):
            attr.restore(amount)
            print(f'Investogator restores stamina. Current value: {self.stamina}')
            self.is_no_longer_unconscious()

    def is_going_insane(self):
        """Set insane to True if sanity drops to 0"""
        if self.sanity == 0:
            self.insane = True
            print("Investigator is driven insane...")

    def is_no_longer_insane(self):
        """Set insane to False if sanity no longer 0"""
        if self.sanity > 0:
            self.insane = False

    def is_going_unconscious(self):
        if self.stamina == 0:
            print("Investigator is knocked unconscious...")
            self.unconscious = True

    def is_no_longer_unconscious(self):
        if self.stamina > 0:
            self.unconscious = False

    def __str__(self):
        """Instance's string representation"""
        return f"INVESTIGATOR DETAILS:\n" \
               f">> {self.sanity}\n" \
               f">> {self.stamina}\n" \
               f">> will: {self.will}\n" \
               f">> fight: {self.fight}"
