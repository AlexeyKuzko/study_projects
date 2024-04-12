import allure
import pytest
import requests

from data import UserHelper, ApiEndpoints, Errors


@allure.story("Проверка создания пользователя")
class TestUserCreate:

    @allure.title("Создать уникального пользователя")
    def test_user_create_unique_true(self, gen_email, gen_pass, gen_name, delete_user):
        payload = {
            "email": gen_email,
            "password": gen_pass,
            "name": gen_name
        }
        response = requests.post(ApiEndpoints.REGISTER, data=payload)
        delete_user.update(response.json())
        assert response.status_code == 200

    @allure.title("Создать пользователя, который уже зарегистрирован")
    def test_user_create_not_unique_false(self, create_user):
        payload = {
            "email": create_user["email"],
            "password": create_user["password"],
            "name": create_user["name"]
        }
        response = requests.post(ApiEndpoints.REGISTER, data=payload)
        assert response.status_code == 403
        assert response.json()["message"].lower() == Errors.USER_ALREADY_EXISTS

    @pytest.mark.parametrize("test_email, test_password, test_name",
                             [["", UserHelper.generate_password(), UserHelper.generate_name()],
                              [UserHelper.generate_email(), "", UserHelper.generate_name()],
                              [UserHelper.generate_email(), UserHelper.generate_password(), ""]])
    @allure.title("Создать пользователя и не заполнить одно из обязательных полей")
    def test_user_create_skip_required_field_false(self, test_email, test_password, test_name):
        payload = {
            "email": test_email,
            "password": test_password,
            "name": test_name
        }
        response = requests.post(ApiEndpoints.REGISTER, data=payload)
        assert response.status_code == 403
        assert response.json()["message"].lower() == Errors.REQUIRED_FIELDS_MISSING
