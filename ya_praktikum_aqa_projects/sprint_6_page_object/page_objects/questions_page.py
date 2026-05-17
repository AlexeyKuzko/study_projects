"""Questions Page support module for Yandex Praktikum Automation QA projects: Sprint 6 Page Object / Page Objects."""

import allure
from page_objects.base_page import BasePage


class ImportantQuestions(BasePage):
    """Page object for the important questions section."""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Нажать на стрелочку у вопроса из списка")
    def click_dropdown_menu_button(self, *locator):
        return self.click_page(*locator)
