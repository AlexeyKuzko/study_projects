from unittest.mock import Mock


class TestDatabase:

    def test_available_buns_count_and_values_true(self, bun, database):
        bun1 = Mock(spec=['name', 'price'])
        bun1.name = "black bun"
        bun1.price = 100

        bun2 = Mock(spec=['name', 'price'])
        bun2.name = "white bun"
        bun2.price = 200

        bun3 = Mock(spec=['name', 'price'])
        bun3.name = "red bun"
        bun3.price = 300

        database.buns = [bun1, bun2, bun3]

        buns = database.available_buns()
        assert len(buns) == 3
        assert all(isinstance(bun, Mock) for bun in buns)

    def test_available_ingredients_count_and_values_true(self, database):
        ingredient1 = Mock(spec=['get_type', 'get_name', 'get_price'])
        ingredient1.get_type.return_value = "SAUCE"
        ingredient1.get_name.return_value = "hot sauce"
        ingredient1.get_price.return_value = 100

        ingredient2 = Mock(spec=['get_type', 'get_name', 'get_price'])
        ingredient2.get_type.return_value = "SAUCE"
        ingredient2.get_name.return_value = "sour cream"
        ingredient2.get_price.return_value = 200

        ingredient3 = Mock(spec=['get_type', 'get_name', 'get_price'])
        ingredient3.get_type.return_value = "SAUCE"
        ingredient3.get_name.return_value = "chili sauce"
        ingredient3.get_price.return_value = 400

        ingredient4 = Mock(spec=['get_type', 'get_name', 'get_price'])
        ingredient4.get_type.return_value = "FILLING"
        ingredient4.get_name.return_value = "cutlet"
        ingredient4.get_price.return_value = 100

        ingredient5 = Mock(spec=['get_type', 'get_name', 'get_price'])
        ingredient5.get_type.return_value = "FILLING"
        ingredient5.get_name.return_value = "dinosaur"
        ingredient5.get_price.return_value = 200

        ingredient6 = Mock(spec=['get_type', 'get_name', 'get_price'])
        ingredient6.get_type.return_value = "FILLING"
        ingredient6.get_name.return_value = "sausage"
        ingredient6.get_price.return_value = 300

        database.ingredients = [ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, ingredient6]

        ingredients = database.available_ingredients()
        assert len(ingredients) == 6
        assert all(isinstance(ingredient, Mock) for ingredient in ingredients)
