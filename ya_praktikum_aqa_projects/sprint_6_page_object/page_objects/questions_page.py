import allure
from page_objects.base_page import BasePage


class ImportantQuestions(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Нажать на стрелочку у вопроса из списка")
    def click_dropdown_menu_button(self, *locator):
        return self.click_page(*locator)
