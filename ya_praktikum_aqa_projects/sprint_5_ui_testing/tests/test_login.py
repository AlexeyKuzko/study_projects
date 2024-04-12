import data
from locators import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:
    def test_login_from_main(self, driver):
        driver.find_element(*Locators.MAIN_AUTH_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(data.TestCredentials.EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(data.TestCredentials.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON)
        )

        assert driver.find_element(*Locators.ORDER_BUTTON).text == "Оформить заказ"

    def test_login_from_personal_acc(self, driver):
        driver.find_element(*Locators.PERSONAL_ACC_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(data.TestCredentials.EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(data.TestCredentials.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON)
        )

        assert driver.find_element(*Locators.ORDER_BUTTON).text == "Оформить заказ"

    def test_login_from_register(self, driver):
        driver.find_element(*Locators.PERSONAL_ACC_BUTTON).click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.LOGIN_LINK).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(data.TestCredentials.EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(data.TestCredentials.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON)
        )

        assert driver.find_element(*Locators.ORDER_BUTTON).text == "Оформить заказ"

    def test_login_from_reset_password(self, driver):
        driver.find_element(*Locators.PERSONAL_ACC_BUTTON).click()
        driver.find_element(*Locators.RESET_PASSWORD_LINK).click()
        driver.find_element(*Locators.RESET_LOGIN_LINK).click()
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(data.TestCredentials.EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(data.TestCredentials.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON)
        )

        assert driver.find_element(*Locators.ORDER_BUTTON).text == "Оформить заказ"
