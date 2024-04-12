import allure
import requests
import random
import string


class Urls:
    BASE_URL = "https://stellarburgers.nomoreparties.site/"
    REGISTER = f"{BASE_URL}api/auth/register"


class UserHelper:

    @staticmethod
    @allure.step("Регистрация тестового пользователя")
    def reg_user():
        payload = {
            "email": UserHelper.generate_email(),
            "password": UserHelper.generate_password(),
            "name": UserHelper.generate_name()
        }
        response = requests.post(Urls.REGISTER, data=payload)
        response.raise_for_status()
        return payload

    @staticmethod
    @allure.step("Генерация email")
    def generate_email():
        email = f'kuzko-alexey5{random.randint(100, 999)}@ya.ru'
        return email

    @staticmethod
    @allure.step("Генерация пароля")
    def generate_password():
        generated_password = ""
        for i in range(7):
            generated_password += random.choice(
                string.ascii_letters + string.digits + string.punctuation
            )
        return generated_password

    @staticmethod
    @allure.step("Генерация имени")
    def generate_name():
        username = ""
        for i in range(random.randint(1, 20)):
            username += random.choice(string.ascii_letters)
        return username
