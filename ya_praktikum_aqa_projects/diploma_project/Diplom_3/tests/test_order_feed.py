import allure

from pages.order_feed_page import OrderFeedPage
from pages.constructor_page import ConstructorPage
from pages.account_page import AccountPage
from locators import OrderFeedPageLocators, ConstructorPageLocators, AccountPageLocators


@allure.story("Проверка раздела «Лента заказов»")
class TestOrderFeed:

    @allure.title("Если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_press_order_get_popup(self, get_driver):
        constructor_page = ConstructorPage(get_driver)
        constructor_page.press_order_feed_link()
        orders_page = OrderFeedPage(get_driver)
        orders_page.find_element(OrderFeedPageLocators.ORDER_FEED_TITLE)
        orders_page.press_order_link()
        assert orders_page.find_element(OrderFeedPageLocators.ORDER_CONTENTS_TITLE).is_displayed()

    @allure.title("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_user_order_displayed_in_feed(self, get_driver, login_user, create_order):
        constructor_page = ConstructorPage(get_driver)
        constructor_page.find_element(ConstructorPageLocators.CONSTRUCTOR_TITLE)
        constructor_page.press_account_link()
        account_page = AccountPage(get_driver)
        account_page.find_element(AccountPageLocators.ORDER_HISTORY_LINK)
        account_page.press_order_history_link()
        account_page.find_element(AccountPageLocators.ORDER_COMPLETED_TEXT)
        user_order = account_page.get_order_number()
        account_page.press_order_feed_link()
        orders_page = OrderFeedPage(get_driver)
        orders_page.find_element(OrderFeedPageLocators.ORDER_FEED_TITLE)
        assert orders_page.find_order_in_order_list(user_order).is_displayed()

    @allure.title("При создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_increment_total_orders_counter(self, get_driver, login_user):
        constructor_page = ConstructorPage(get_driver)
        constructor_page.find_element(ConstructorPageLocators.CONSTRUCTOR_TITLE)
        constructor_page.press_order_feed_link()
        orders_page = OrderFeedPage(get_driver)
        orders_page.find_element(OrderFeedPageLocators.ORDER_FEED_TITLE)
        total_orders_count = orders_page.get_total_orders_number()
        orders_page.press_constructor_link()
        constructor_page.find_element(ConstructorPageLocators.CONSTRUCTOR_TITLE)
        constructor_page.create_order()
        orders_page.press_order_feed_link()
        orders_page.find_element(OrderFeedPageLocators.ORDER_FEED_TITLE)
        assert int(orders_page.get_total_orders_number()) == (int(total_orders_count) + 1)

    @allure.title("При создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_increment_today_orders_counter(self, get_driver, login_user):
        constructor_page = ConstructorPage(get_driver)
        constructor_page.find_element(ConstructorPageLocators.CONSTRUCTOR_TITLE)
        constructor_page.press_order_feed_link()
        orders_page = OrderFeedPage(get_driver)
        orders_page.find_element(OrderFeedPageLocators.ORDER_FEED_TITLE)
        today_orders_count = orders_page.get_today_orders_number()
        orders_page.press_constructor_link()
        constructor_page.find_element(ConstructorPageLocators.CONSTRUCTOR_TITLE)
        constructor_page.create_order()
        constructor_page.press_order_feed_link()
        orders_page.find_element(OrderFeedPageLocators.ORDER_FEED_TITLE)
        assert int(orders_page.get_today_orders_number()) == (int(today_orders_count) + 1)

    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    def test_create_order_get_number_in_work_list(self, get_driver, login_user):
        constructor_page = ConstructorPage(get_driver)
        constructor_page.find_element(ConstructorPageLocators.CONSTRUCTOR_TITLE)
        created_order = constructor_page.create_order()
        constructor_page.press_order_feed_link()
        orders_page = OrderFeedPage(get_driver)
        orders_page.find_element(OrderFeedPageLocators.ORDER_NUMBER_IN_WORK)
        assert int(orders_page.get_order_number_in_work_list()) == int(created_order)
