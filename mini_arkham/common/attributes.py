class Attribute:

    def __init__(self, name: str, max_value: int):
        """"""
        self.name = name
        self.value = max_value
        self.max_value = max_value

    def reduce(self, amount: int) -> None:
        """Decreases value by the provided amount, down to min 0"""
        self.value = max(0, self.value - amount)

    def restore(self, amount: int) -> None:
        """Increases value by the provided amount, up to max_value"""
        self.value = min(self.max_value, self.value + amount)

    def __str__(self):
        """Instance's string representation"""
        return f"{self.name}: {self.value} ({self.max_value})"

    def __get__(self):
        """Returns the value parameter once an instance is within another object"""
        return self.value

    def __eq__(self, other: int):
        """Allows to compare attribute value to int"""
        return self.value == other

    def __gt__(self, other: int):
        """Allows asserting value > int"""
        return self.value > other


class Sanity(Attribute):
    name = "Sanity"

    def __init__(self, max_value: int = 7):
        Attribute.__init__(self, self.name, max_value)


class Stamina(Attribute):
    name = "Stamina"

    def __init__(self, max_value: int = 7):
        Attribute.__init__(self, self.name, max_value)