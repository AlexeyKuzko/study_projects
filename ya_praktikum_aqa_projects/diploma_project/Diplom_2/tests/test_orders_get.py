import allure

from data import OrderHelper, Errors


@allure.story("Проверка получения заказов конкретного пользователя")
class TestOrdersGet:

    @allure.title("Получение заказов - авторизованный пользователь")
    def test_get_orders_auth_user_true(self, valid_hashes, create_user):
        OrderHelper.create_order(valid_hashes, create_user["response_json"]["accessToken"])
        OrderHelper.create_order(valid_hashes, create_user["response_json"]["accessToken"])
        response = OrderHelper.get_order_list(create_user["response_json"]["accessToken"])
        assert response.status_code == 200
        assert len(response.json()["orders"]) == 2

    @allure.title("Получение заказов - неавторизованный пользователь")
    def test_get_orders_unauth_user_false(self, valid_hashes, create_user):
        OrderHelper.create_order(valid_hashes)
        OrderHelper.create_order(valid_hashes)
        response = OrderHelper.get_order_list()
        assert response.status_code == 401
        assert response.json()["message"].lower() == Errors.USER_UNAUTHORIZED
