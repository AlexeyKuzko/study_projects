import allure

from pages.base_page import BasePage
from locators import AccountPageLocators


class AccountPage(BasePage):

    @allure.step("Нажать кнопку «Выход»")
    def press_logout_button(self):
        self.press_element(AccountPageLocators.LOGOUT_BUTTON)

    @allure.step("Нажать ссылку «История заказов»")
    def press_order_history_link(self):
        self.press_element(AccountPageLocators.ORDER_HISTORY_LINK)

    @allure.step("Получаем номер последнего заказа в разделе «История заказов»")
    def get_order_number(self):
        return self.get_text_from_element(AccountPageLocators.ORDER_NUMBER_IN_ORDER_HISTORY)
