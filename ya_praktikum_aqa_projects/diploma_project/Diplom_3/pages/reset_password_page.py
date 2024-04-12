import allure

from pages.base_page import BasePage
from locators import BasePageLocators, ResetPasswordPageLocators


class ResetPasswordPage(BasePage):

    @allure.step("Ввод почты")
    def fill_email(self, email):
        self.fill_field(BasePageLocators.EMAIL_FIELD, email)

    @allure.step("Клик по кнопке «Восстановить»")
    def press_reset_pass_button(self):
        self.press_element(ResetPasswordPageLocators.RESET_BUTTON)

    @allure.step("Клик по кнопке показать/скрыть пароль")
    def press_show_password_icon(self):
        self.move_to_element_and_press(ResetPasswordPageLocators.SHOW_PASSWORD_ICON)
