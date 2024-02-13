import data
from locators import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestGoToConstructor:
    def test_go_from_personal_acc_to_constructor(self, driver):
        driver.get(data.TestUrls.LOGIN_PAGE)
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(data.TestCredentials.EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(data.TestCredentials.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.PERSONAL_ACC_BUTTON).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON)
        )

        assert data.TestUrls.MAIN_PAGE == driver.current_url

    def test_go_from_personal_acc_to_constructor_by_logo(self, driver):
        driver.get(data.TestUrls.LOGIN_PAGE)
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(data.TestCredentials.EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(data.TestCredentials.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.PERSONAL_ACC_BUTTON).click()
        driver.find_element(*Locators.LOGO_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON)
        )

        assert data.TestUrls.MAIN_PAGE == driver.current_url
