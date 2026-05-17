"""Solution for Yandex Praktikum Automation QA projects: Diploma Project / Diplom 1 / Praktikum / Burger."""

from typing import List

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class Burger:
    """
    Модель бургера.
    Бургер состоит из булочек и ингредиентов (начинка или соус).
    Ингредиенты можно перемещать и удалять.
    Можно распечать чек с информацией о бургере.
    """

    def __init__(self):
        self.bun = None
        self.ingredients: List[Ingredient] = []

    def set_buns(self, bun: Bun):
        """Set the buns."""
        self.bun = bun

    def add_ingredient(self, ingredient: Ingredient):
        """Add the ingredient."""
        self.ingredients.append(ingredient)

    def remove_ingredient(self, index: int):
        """Remove the ingredient."""
        del self.ingredients[index]

    def move_ingredient(self, index: int, new_index: int):
        """Move the ingredient."""
        self.ingredients.insert(new_index, self.ingredients.pop(index))

    def get_price(self) -> float:
        """Return the price."""
        price = self.bun.get_price() * 2

        for ingredient in self.ingredients:
            price += ingredient.get_price()

        return price

    def get_receipt(self) -> str:
        """Return the receipt."""
        receipt: List[str] = [f"(==== {self.bun.get_name()} ====)"]

        for ingredient in self.ingredients:
            receipt.append(f"= {str(ingredient.get_type()).lower()} {ingredient.get_name()} =")

        receipt.append(f"(==== {self.bun.get_name()} ====)\n")
        receipt.append(f"Price: {self.get_price()}")

        return "\n".join(receipt)
