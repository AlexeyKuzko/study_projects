import json

import allure
import pytest

from helpers.api_client import CourierRequests


@allure.feature('Проверка регистрации курьера')
class TestCourierRegister:

    @allure.title('Проверяем, что курьера можно создать')
    def test_registration_login(self, create_user_payload):
        crr = CourierRequests()
        response = crr.create_courier_post(create_user_payload)
        assert response['ok']

    @allure.title('Проверяем, что нельзя создать двух одинаковых курьеров')
    def test_create_existing_courier_login(self, create_user_payload):
        crr = CourierRequests()
        payload = create_user_payload
        crr.create_courier_post(payload)
        response = crr.login_courier_post(payload)
        response_double = crr.create_courier_post(payload, status=409)
        courier_id = response["id"]
        crr.delete_courier(courier_id=courier_id)
        assert response_double["message"] == "Этот логин уже используется. Попробуйте другой."

    @pytest.mark.parametrize("payload_data",
                             [
                                 ['', '0000', 'John'],
                                 ['pupa', '', 'Bob'],
                                 ['', '', 'Alice'],
                                 ['', '4321', ''],
                                 ['lupa', '', '']
                             ])
    @allure.title('Проверка, что без обязательных данных (логин, пароль) курьер не создается')
    def test_required_fields_on_register(self, payload_data):
        crr = CourierRequests()
        payload = json.dumps(payload_data)
        response = crr.create_courier_post(payload, status=400)
        assert response["message"] == "Недостаточно данных для создания учетной записи"
