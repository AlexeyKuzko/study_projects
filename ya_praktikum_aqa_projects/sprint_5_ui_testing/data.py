import random
import string


class TestUrls:
    MAIN_PAGE = "https://stellarburgers.nomoreparties.site/"
    REG_PAGE = f"{MAIN_PAGE}register"
    LOGIN_PAGE = f"{MAIN_PAGE}login"
    PERSONAL_ACCOUNT_PAGE = f"{MAIN_PAGE}account/profile"


class TestCredentials:
    NAME = "Alexey Kuzko"
    EMAIL = "alexeykuzko5555@ya.ru"
    PASSWORD = "123Abc"

    @staticmethod
    def bad_password(pass_len=5):
        generated_password = ""
        for i in range(int(pass_len)):
            generated_password += random.choice(
                string.ascii_letters + string.digits + string.punctuation
            )
        return generated_password
