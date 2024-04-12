import allure

from pages.login_page import LoginPage
from pages.constructor_page import ConstructorPage
from pages.reset_password_page import ResetPasswordPage
from locators import ResetPasswordPageLocators as reset_pass_locators


@allure.story("Проверка восстановления пароля")
class TestResetPassword:

    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_reset_link_redirects_to_reset_page(self, get_driver):
        constructor_page = ConstructorPage(get_driver)
        constructor_page.press_enter_account_button()
        login_page = LoginPage(get_driver)
        login_page.press_reset_password_link()
        reset_pass_page = ResetPasswordPage(get_driver)
        assert reset_pass_page.find_element(reset_pass_locators.RESET_BUTTON).is_displayed()

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_fill_email_press_reset_button(self, get_driver, gen_email):
        constructor_page = ConstructorPage(get_driver)
        constructor_page.press_enter_account_button()
        login_page = LoginPage(get_driver)
        login_page.press_reset_password_link()
        reset_pass_page = ResetPasswordPage(get_driver)
        reset_pass_page.fill_email(gen_email)
        reset_pass_page.press_reset_pass_button()
        assert reset_pass_page.find_element(reset_pass_locators.SAVE_BUTTON).is_displayed()

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_show_pass_makes_field_active(self, get_driver, gen_email):
        constructor_page = ConstructorPage(get_driver)
        constructor_page.press_enter_account_button()
        login_page = LoginPage(get_driver)
        login_page.press_reset_password_link()
        reset_pass_page = ResetPasswordPage(get_driver)
        reset_pass_page.fill_email(gen_email)
        reset_pass_page.press_reset_pass_button()
        reset_pass_page.find_element(reset_pass_locators.SAVE_BUTTON)
        reset_pass_page.press_show_password_icon()
        assert reset_pass_page.find_element(reset_pass_locators.PASSWORD_FIELD_ACTIVE).is_displayed()
