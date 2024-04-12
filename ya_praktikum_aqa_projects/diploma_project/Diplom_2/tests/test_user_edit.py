import allure
import pytest
import requests

from data import ApiEndpoints, Errors


@allure.story("Проверка изменения данных пользователя")
class TestUserEdit:
    @allure.title("Изменение данных пользователя с авторизацией")
    @pytest.mark.parametrize("payload", ["email", "name"])
    def test_authorized_user_edit_true(self, create_user, gen_name, payload):
        payload = {payload: gen_name}
        response = requests.patch(ApiEndpoints.USER, data=payload,
                                  headers={"Authorization": f'{create_user["response_json"]["accessToken"]}'})
        assert response.status_code == 200
        assert response.json()["user"][list(payload.keys())[0]] == payload[list(payload.keys())[0]]

    @allure.title("Изменение данных пользователя  без авторизации")
    @pytest.mark.parametrize("payload", ["email", "name"])
    def test_unauthorized_user_edit_false(self, create_user, gen_name, payload):
        payload = {payload: gen_name}
        response = requests.patch(ApiEndpoints.USER, data=payload)
        assert response.status_code == 401
        assert response.json()["message"].lower() == Errors.USER_UNAUTHORIZED
