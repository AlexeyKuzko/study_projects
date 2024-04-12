import json

import allure
import pytest
from faker import Faker

from helpers.api_client import CourierRequests

faker = Faker()


@pytest.fixture
@allure.step('Конструируем запрос для отправки заказа')
def create_order_payload():
    fake_date = faker.date_between(start_date='today', end_date='+1y')
    date = fake_date.strftime("%Y-%m-%d")
    payload = {
        "firstName": faker.first_name(),
        "lastName": faker.last_name(),
        "address": faker.address(),
        "metroStation": 1,
        "phone": "+76665551122",
        "rentTime": 2,
        "deliveryDate": date,
        "comment": "Комментирую!"
    }
    return payload


@pytest.fixture
@allure.step('Создание курьера, логин и удаление')
def create_courier_login_and_delete(create_user_payload):
    payload = create_user_payload
    response = CourierRequests.create_courier_post(payload)
    login_response = CourierRequests.login_courier_post(payload)
    CourierRequests.delete_courier(courier_id=login_response["id"])
    return login_response


@pytest.fixture
@allure.step('Создание данных курьера')
def create_user_payload():
    data = {
        "firstName": faker.name(),
        "login": faker.name(),
        "password": faker.pyint()
    }
    return json.dumps(data)
