import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators
from data import Urls


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть стартовую страницу")
    def open_base_url(self):
        return self.driver.get(Urls.BASE_URL)

    @allure.step("Вернуть адрес текущей страницы")
    def show_current_url(self):
        return self.driver.current_url

    @allure.step("Найти страницу или элемент")
    def find_page(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Нажать на страницу или элемент")
    def click_page(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step("Открыть блок 'Вопросы о важном'")
    def open_important_questions_section(self):
        element = self.find_page(BasePageLocators.important_questions_section)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликаем кнопку 'Заказать' в хэдере")
    def click_header_booking_button(self):
        return self.driver.find_element(*BasePageLocators.header_booking_button).click()

    @allure.step("Дождаться загрузки элемента")
    def wait_until_element_is_visible(self, locator):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(locator)
        )

    @allure.step("Дождаться, чтобы на элемент можно было нажать")
    def wait_until_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(locator)
        )

    @allure.step("Принять cookies")
    def click_cookie_consent(self):
        return self.driver.find_element(*BasePageLocators.cookie_consent_button).click()

    @allure.step("Открыть и проверить новое окно")
    def check_window(self):
        original_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
