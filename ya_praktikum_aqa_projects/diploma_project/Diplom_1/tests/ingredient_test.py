import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
    ])
    def test_init_attributes_accepts_named_params_true(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price

    def test_get_price_returns_correct_price_true(self, sauce_ingredient, filling_ingredient):
        assert sauce_ingredient.get_price() == 200
        assert filling_ingredient.get_price() == 300

    def test_get_name_return_correct_name_true(self, sauce_ingredient, filling_ingredient):
        assert sauce_ingredient.get_name() == "sour cream"
        assert filling_ingredient.get_name() == "sausage"

    def test_get_type_return_correct_type_true(self, sauce_ingredient, filling_ingredient):
        assert sauce_ingredient.get_type() == INGREDIENT_TYPE_SAUCE
        assert filling_ingredient.get_type() == INGREDIENT_TYPE_FILLING
