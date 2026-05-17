"""Automated test cases for Order Create in Yandex Praktikum Automation QA projects: Sprint 7 API Testing."""

import allure
import pytest

from helpers.api_client import OrderApiClient


@allure.feature("Проверка создания заказа")
class TestOrderCreation:
    @allure.title('Проверка возможности заказать с разными цветами, ответ содержит "track"')
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], None])
    def test_create_order_successful(self, color, create_order_payload):
        orr = OrderApiClient()
        payload = create_order_payload
        response = orr.create_order_post(payload)
        assert "track" in response.keys()
