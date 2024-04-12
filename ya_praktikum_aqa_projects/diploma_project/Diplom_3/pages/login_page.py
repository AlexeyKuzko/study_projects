import allure

from pages.base_page import BasePage
from locators import BasePageLocators, LoginPageLocators


class LoginPage(BasePage):

    @allure.step("Нажать кнопку Восстановить пароль")
    def press_reset_password_link(self):
        self.press_element(LoginPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step("Нажать кнопку Войти")
    def press_enter_button(self):
        self.press_element(LoginPageLocators.ENTER_BUTTON)

    @allure.step("Ввести email на странице Вход")
    def fill_email_field(self, email):
        self.fill_field(BasePageLocators.EMAIL_FIELD, email)

    @allure.step("Ввести пароль на странице Вход")
    def fill_password_field(self, password):
        self.fill_field(BasePageLocators.PASSWORD_FIELD, password)
