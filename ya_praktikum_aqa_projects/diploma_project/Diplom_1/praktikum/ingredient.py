"""Solution for Yandex Praktikum Automation QA projects: Diploma Project / Diplom 1 / Praktikum / Ingredient."""


class Ingredient:
    """
    Модель ингредиента.
    Ингредиент: начинка или соус.
    У ингредиента есть тип (начинка или соус), название и цена.
    """

    def __init__(self, ingredient_type: str, name: str, price: float):
        self.type = ingredient_type
        self.name = name
        self.price = price

    def get_price(self) -> float:
        """Return the price."""
        return self.price

    def get_name(self) -> str:
        """Return the name."""
        return self.name

    def get_type(self) -> str:
        """Return the type."""
        return self.type
