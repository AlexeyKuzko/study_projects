import allure
import pytest

from data import UserHelper, Errors


@allure.story("Проверка логина пользователя")
class TestUserLogin:
    @allure.title("Логин под существующим пользователем")
    def test_existing_user_login_true(self, create_user):
        response = UserHelper.login_user(create_user["email"], create_user["password"])
        assert response.status_code == 200

    @pytest.mark.parametrize("login, password",
                             [("test_name", UserHelper.generate_password()),
                              (UserHelper.generate_email(), "test_password")])
    @allure.title("Логин с неверным логином и паролем")
    def test_login_invalid_credentials_false(self, create_user, login, password):
        response = UserHelper.login_user(login, password)
        assert response.status_code == 401
        assert response.json()["message"] == Errors.INCORRECT_CREDENTIALS
