import allure

from pages.base_page import BasePage
from locators import OrderFeedPageLocators as order_locators


class OrderFeedPage(BasePage):

    @allure.step("Кликнуть на заказ")
    def press_order_link(self):
        self.press_element(order_locators.ORDER_IN_FEED_LINK)

    @allure.step("Найти заказ")
    def find_order_in_order_list(self, chosen_order):
        method, locator = order_locators.ORDER_NUMBER_IN_ORDER_FEED
        locator = locator.format(chosen_order)
        return self.find_element((method, locator))

    @allure.step("Получить значение счетчика Выполнено за всё время")
    def get_total_orders_number(self):
        return self.get_text_from_element(order_locators.COMPLETE_ORDERS_COUNT_TOTAL)

    @allure.step("Получить значение счетчика Выполнено за сегодня")
    def get_today_orders_number(self):
        return self.get_text_from_element(order_locators.COMPLETE_ORDERS_COUNT_TODAY)

    @allure.step("Получить значение счетчика В работе")
    def get_order_number_in_work_list(self):
        return self.get_text_from_element(order_locators.ORDER_NUMBER_IN_WORK)
