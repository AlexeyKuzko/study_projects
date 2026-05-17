"""Data module for Yandex Praktikum Automation QA projects: Sprint 7 API Testing / Helpers."""


class Urls:
    """Store service endpoint URLs used by API tests."""

    BASE_URL = "https://qa-scooter.praktikum-services.ru/"
    ORDER_URL = f"{BASE_URL}api/v1/orders/"
    COURIER_URL = f"{BASE_URL}api/v1/courier/"
    COURIER_LOGIN_URL = f"{BASE_URL}api/v1/courier/login"
