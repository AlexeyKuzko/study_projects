import allure

from data import OrderHelper, Errors


@allure.story("Проверка создания заказа")
class TestOrderCreate:

    @allure.title("Создание заказа c авторизацией")
    def test_order_create_authorized_true(self, valid_hashes, create_user):
        response = OrderHelper.create_order(valid_hashes, create_user["response_json"]["accessToken"])
        assert response.json()["order"]["owner"]["name"] == create_user["name"]

    @allure.title("Создание заказа без авторизации")
    def test_order_create_unauthorized_true(self, valid_hashes):
        response = OrderHelper.create_order(valid_hashes)
        assert response.status_code == 200
        assert "order" and "name" in response.json()

    @allure.title("Создание заказа без ингредиентов")
    def test_order_create_empty_false(self):
        response = OrderHelper.create_order("")
        assert response.status_code == 400
        assert response.json()["message"].lower() == Errors.INGREDIENT_ID_NOT_PROVIDED

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_order_create_incorrect_hash_false(self, invalid_hashes):
        response = OrderHelper.create_order(invalid_hashes)
        assert response.status_code == 400
        assert response.json()["message"].lower() == Errors.INGREDIENT_ID_INCORRECT
