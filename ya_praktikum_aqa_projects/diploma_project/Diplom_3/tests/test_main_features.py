import allure

from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderFeedPage
from locators import OrderFeedPageLocators, ConstructorPageLocators


@allure.story("Проверка основного функционала")
class TestMainFeatures:

    @allure.title("Переход по клику на «Конструктор»")
    def test_redirect_by_constructor_button(self, get_driver):
        constructor_page = ConstructorPage(get_driver)
        constructor_page.press_order_feed_link()
        orders_page = OrderFeedPage(get_driver)
        orders_page.find_element(OrderFeedPageLocators.ORDER_FEED_TITLE)
        constructor_page.press_constructor_link()
        assert constructor_page.find_element(ConstructorPageLocators.CONSTRUCTOR_TITLE).is_displayed()

    @allure.title("Переход по клику на «Лента заказов»")
    def test_redirect_by_order_list_button(self, get_driver):
        constructor_page = ConstructorPage(get_driver)
        constructor_page.press_order_feed_link()
        orders_page = OrderFeedPage(get_driver)
        assert orders_page.find_element(OrderFeedPageLocators.ORDER_FEED_TITLE).is_displayed()

    @allure.title("Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_get_ingredient_details(self, get_driver):
        constructor_page = ConstructorPage(get_driver)
        constructor_page.press_ingredient()
        assert constructor_page.find_element(ConstructorPageLocators.INGREDIENT_DETAILS_TITLE).is_displayed()

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_close_ingredient_details_window(self, get_driver):
        constructor_page = ConstructorPage(get_driver)
        constructor_page.press_ingredient()
        constructor_page.find_element(ConstructorPageLocators.INGREDIENT_DETAILS_TITLE)
        constructor_page.press_close_button()
        assert constructor_page.wait_until_element_invisible(ConstructorPageLocators.INGREDIENT_DETAILS_MODAL)

    @allure.title("При добавлении ингредиента в заказ счётчик этого ингридиента увеличивается")
    def test_ingredient_counter_change(self, get_driver):
        constructor_page = ConstructorPage(get_driver)
        original_number = constructor_page.get_counter_number_of_ingredient_bun()
        constructor_page.move_bun_to_cart()
        current_number = constructor_page.get_counter_number_of_ingredient_bun()
        assert int(current_number) > int(original_number)

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_successful_order(self, get_driver, login_user):
        constructor_page = ConstructorPage(get_driver)
        constructor_page.find_element(ConstructorPageLocators.INGREDIENT_BUN)
        constructor_page.move_bun_to_cart()
        constructor_page.move_sauce_to_cart()
        constructor_page.move_filling_to_cart()
        constructor_page.find_element(ConstructorPageLocators.ORDER_CREATE_BUTTON)
        constructor_page.press_order_button()
        constructor_page.find_element(ConstructorPageLocators.ORDER_NUMBER_IN_CONSTRUCTOR)
        assert constructor_page.find_element(ConstructorPageLocators.ORDER_IS_PREPARING_TEXT).is_displayed()
