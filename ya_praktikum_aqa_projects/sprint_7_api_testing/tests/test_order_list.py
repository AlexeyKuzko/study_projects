"""Automated test cases for Order List in Yandex Praktikum Automation QA projects: Sprint 7 API Testing."""

import allure

from helpers.api_client import OrderApiClient

order_client = OrderApiClient()


@allure.feature("Order list API test")
class TestOrderList:
    @allure.title("API returns order list")
    def test_order_list_endpoint(self):
        response = order_client.get_orders_list()
        assert "orders" in response.keys()
