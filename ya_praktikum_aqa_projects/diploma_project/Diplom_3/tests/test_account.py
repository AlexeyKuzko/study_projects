import allure

from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.constructor_page import ConstructorPage
from locators import ConstructorPageLocators, LoginPageLocators, AccountPageLocators


@allure.story("Проверка Личного кабинета")
class TestAccountPage:

    @allure.title("Переход по клику на «Личный кабинет»")
    def test_account_link_redirect(self, get_driver, login_user):
        constructor_page = ConstructorPage(get_driver)
        constructor_page.find_element(ConstructorPageLocators.CONSTRUCTOR_TITLE)
        constructor_page.press_account_link()
        account_page = AccountPage(get_driver)
        assert account_page.find_element(AccountPageLocators.PROFILE_LINK).is_displayed()

    @allure.title("Переход в раздел «История заказов»")
    def test_redirect_to_order_history(self, get_driver, login_user, create_order):
        constructor_page = ConstructorPage(get_driver)
        constructor_page.find_element(ConstructorPageLocators.CONSTRUCTOR_TITLE)
        constructor_page.press_account_link()
        account_page = AccountPage(get_driver)
        account_page.find_element(AccountPageLocators.ORDER_HISTORY_LINK)
        account_page.press_order_history_link()
        assert account_page.find_element(AccountPageLocators.ORDER_COMPLETED_TEXT).is_displayed()

    @allure.title("Выход из аккаунта")
    def test_account_logout_via_button(self, get_driver, login_user):
        constructor_page = ConstructorPage(get_driver)
        constructor_page.find_element(ConstructorPageLocators.CONSTRUCTOR_TITLE)
        constructor_page.press_account_link()
        account_page = AccountPage(get_driver)
        account_page.find_element(AccountPageLocators.LOGOUT_BUTTON)
        account_page.press_logout_button()
        login_page = LoginPage(get_driver)
        assert login_page.find_element(LoginPageLocators.ENTER_BUTTON).is_displayed()
