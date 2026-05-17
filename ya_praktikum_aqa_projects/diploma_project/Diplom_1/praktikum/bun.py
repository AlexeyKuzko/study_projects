"""Solution for Yandex Praktikum Automation QA projects: Diploma Project / Diplom 1 / Praktikum / Bun."""


class Bun:
    """
    Модель булочки для бургера.
    Булочке можно дать название и назначить цену.
    """

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_name(self) -> str:
        """Return the name."""
        return self.name

    def get_price(self) -> float:
        """Return the price."""
        return self.price
