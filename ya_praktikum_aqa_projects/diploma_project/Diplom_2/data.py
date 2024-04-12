import random
import string

import allure
import requests


class ApiEndpoints:
    BASE_URL = "https://stellarburgers.nomoreparties.site/api/"
    REGISTER = f"{BASE_URL}auth/register"
    LOGIN = f"{BASE_URL}auth/login"
    USER = f"{BASE_URL}auth/user"
    ORDERS = f"{BASE_URL}orders"


class UserHelper:

    @staticmethod
    @allure.step("Регистрация тестового юзера")
    def reg_user():
        with allure.step("Генерация данных юзера"):
            name = UserHelper.generate_name()
            password = UserHelper.generate_password()
            email = UserHelper.generate_email()
        with allure.step("Отправка данных для регистрации"):
            payload = {"email": email, "password": password, "name": name}
            response = requests.post(ApiEndpoints.REGISTER, json=payload)
            response.raise_for_status()
        with allure.step("Обработка ответа на регистрацию"):
            user_data = {
                "email": email,
                "name": name,
                "password": password,
                "response_json": response.json(),
            }

        return user_data

    @staticmethod
    @allure.step("Генерация тестового email")
    def generate_email():
        email = f"alexey_kuzko5{random.randint(100, 999)}@ya.ru"
        return email

    @staticmethod
    @allure.step("Генерация тестового пароля")
    def generate_password():
        generated_password = ""
        for i in range(7):
            generated_password += random.choice(
                string.ascii_letters + string.digits + string.punctuation
            )
        return generated_password

    @staticmethod
    @allure.step("Генерация тестового имени")
    def generate_name():
        username = ""
        for i in range(random.randint(1, 20)):
            username += random.choice(string.ascii_lowercase)
        return username

    @staticmethod
    @allure.step("Логин пользователя")
    def login_user(email, password):
        payload = {
            "email": email,
            "password": password,
        }

        response = requests.post(ApiEndpoints.LOGIN, json=payload)
        return response

    @staticmethod
    @allure.step("Удаление тестового юзера")
    def delete_user(access_token):
        headers = {"Authorization": access_token}
        requests.delete(ApiEndpoints.USER, headers=headers)


class OrderHelper:
    @staticmethod
    @allure.step("Создание заказа")
    def create_order(ingredients, access_token=None):
        with allure.step("Подготовка данных для создания заказа"):
            payload = {"ingredients": [ingredients]}
        with allure.step("Отправка запроса на создание заказа"):
            headers = {"Authorization": access_token}
            response = requests.post(ApiEndpoints.ORDERS, data=payload, headers=headers)
            return response

    @staticmethod
    @allure.step("Получение списка заказов")
    def get_order_list(access_token=None):
        with allure.step("Отправка запроса на получение списка заказов"):
            headers = {"Authorization": access_token}
            response = requests.get(ApiEndpoints.ORDERS, headers=headers)
            return response


class IngredientsHash:
    VALID_INGREDIENTS_HASH = (
        "61c0c5a71d1f82001bdaaa6d",
        "61c0c5a71d1f82001bdaaa73",
        "61c0c5a71d1f82001bdaaa77",
        "61c0c5a71d1f82001bdaaa7a",
        "61c0c5a71d1f82001bdaaa72",
        "61c0c5a71d1f82001bdaaa70",
        "61c0c5a71d1f82001bdaaa71",
        "61c0c5a71d1f82001bdaaa6d",
        "61c0c5a71d1f82001bdaaa6e",
        "61c0c5a71d1f82001bdaaa74",
        "61c0c5a71d1f82001bdaaa76",
        "61c0c5a71d1f82001bdaaa77",
        "61c0c5a71d1f82001bdaaa78",
        "61c0c5a71d1f82001bdaaa79",
        "61c0c5a71d1f82001bdaaa73",
        "61c0c5a71d1f82001bdaaa6f",
        "61c0c5a71d1f82001bdaaa75",
        "61c0c5a71d1f82001bdaaa6c"
    )

    @classmethod
    @allure.step("Получить неверные хэши ингредиентов")
    def generate_invalid_hashes(cls):
        invalid_hashes = []
        for valid_hash in cls.VALID_INGREDIENTS_HASH:
            invalid_hash_list = list(valid_hash)
            random.shuffle(invalid_hash_list)
            invalid_hashes.append("".join(invalid_hash_list))
        return tuple(invalid_hashes)


class Errors:
    INCORRECT_CREDENTIALS = "email or password are incorrect"
    INGREDIENT_ID_INCORRECT = "one or more ids provided are incorrect"
    INGREDIENT_ID_NOT_PROVIDED = "ingredient ids must be provided"
    REQUIRED_FIELDS_MISSING = "email, password and name are required fields"
    USER_ALREADY_EXISTS = "user already exists"
    USER_UNAUTHORIZED = "you should be authorised"
