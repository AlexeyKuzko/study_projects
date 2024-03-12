import json

import allure
import requests
from faker import Faker

from helpers.data import Urls

fake = Faker()


class BaseRequests:

    @staticmethod
    def make_request_and_check(method, url, data=None, status=None):
        allowed_methods = ['get', 'post', 'put', 'delete']
        assert method.lower() in allowed_methods, f"Invalid HTTP method: {method}"

        response = None
        if method.lower() == 'get':
            response = requests.get(url=url)
        elif method.lower() == 'post':
            response = requests.post(url=url, data=data, headers={'Content-Type': 'application/json'})
        elif method.lower() == 'put':
            response = requests.put(url=url, data=data)
        elif method.lower() == 'delete':
            response = requests.delete(url=url, data=data)

        assert response.status_code == status, f"Unexpected status code: {response.status_code}"

        if 'application/json' in response.headers['Content-Type']:
            return response.json()
        else:
            return response.text


class OrderApiClient(BaseRequests):

    def __init__(self):
        super().__init__()

    @allure.step('Создаем заказ (POST). Ожидаем response-status {status}')
    def create_order_post(self, data=None, status=201):
        url = Urls.ORDER_URL
        return self.make_request_and_check('post', url, data=json.dumps(data), status=status)

    @allure.step('Получаем список заказов (GET). Ожидаем response-status {status}')
    def get_orders_list(self, status=200):
        url = Urls.ORDER_URL
        return self.make_request_and_check('get', url, status=status)


class CourierRequests(BaseRequests):

    def __init__(self):
        super().__init__()

    @allure.step('Создаем курьера (POST). Ожидаем response-status {status}')
    def create_courier_post(self, data=None, status=201):
        url = Urls.COURIER_URL
        return self.make_request_and_check('post', url, data=data, status=status)

    @allure.step('Залогиниваем курьера (POST). Ожидаем response-status {status}')
    def login_courier_post(self, data=None, status=200):
        url = Urls.COURIER_LOGIN_URL
        return self.make_request_and_check('post', url, data=data, status=status)

    @allure.step('Удаляем курьера (DELETE). Ожидаем response-status {status}')
    def delete_courier(self, data=None, courier_id=None, status=200):
        url = f'{Urls.COURIER_URL}{courier_id}'
        return self.make_request_and_check('delete', url, data=data, status=status)

    @staticmethod
    def create_login_payload(login, password):
        data = {
            "login": login,
            "password": password
        }
        return json.dumps(data)
