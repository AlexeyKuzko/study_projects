import allure

from pages.base_page import BasePage
from locators import BasePageLocators, ConstructorPageLocators


class ConstructorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажать кнопку Войти в аккаунт")
    def press_enter_account_button(self):
        self.move_to_element_and_press(ConstructorPageLocators.ENTER_ACCOUNT_BUTTON)

    @allure.step("Нажать на ингредиент")
    def press_ingredient(self):
        self.move_to_element_and_press(ConstructorPageLocators.INGREDIENT_BUN)

    @allure.step("Нажать кнопку закрытия в окне ингредиента")
    def press_close_button(self):
        self.move_to_element_and_press(BasePageLocators.CLOSE_BUTTON)

    @allure.step("Нажать кнопку Оформить заказ")
    def press_order_button(self):
        self.move_to_element_and_press(ConstructorPageLocators.ORDER_CREATE_BUTTON)

    @allure.step("Получить значение счетчика ингредиентов")
    def get_counter_number_of_ingredient_bun(self):
        return self.get_text_from_element(ConstructorPageLocators.INGREDIENT_COUNTER)

    @allure.step("Перенести булку в корзину")
    def move_bun_to_cart(self):
        self.move_element(ConstructorPageLocators.INGREDIENT_BUN, ConstructorPageLocators.ORDER_CART)

    @allure.step("Перенести соус в корзину")
    def move_sauce_to_cart(self):
        self.move_element(ConstructorPageLocators.INGREDIENT_SAUCE, ConstructorPageLocators.ORDER_CART)

    @allure.step("Перенести начинку в корзину")
    def move_filling_to_cart(self):
        self.move_element(ConstructorPageLocators.INGREDIENT_FILLING, ConstructorPageLocators.ORDER_CART)

    @allure.step("Создать заказ")
    def create_order(self):
        self.find_element(ConstructorPageLocators.INGREDIENT_BUN)
        self.move_element(ConstructorPageLocators.INGREDIENT_BUN, ConstructorPageLocators.ORDER_CART)
        self.move_element(ConstructorPageLocators.INGREDIENT_FILLING, ConstructorPageLocators.ORDER_CART)
        self.find_element(ConstructorPageLocators.ORDER_CREATE_BUTTON)
        self.move_to_element_and_press(ConstructorPageLocators.ORDER_CREATE_BUTTON)
        self.find_element(ConstructorPageLocators.ORDER_IS_PREPARING_TEXT)
        self.wait_until_element_invisible(ConstructorPageLocators.DEFAULT_ORDER_NUMBER)
        created_order = self.get_text_from_element(ConstructorPageLocators.ORDER_NUMBER_IN_CONSTRUCTOR)
        self.move_to_element_and_press(BasePageLocators.CLOSE_BUTTON)
        return created_order
