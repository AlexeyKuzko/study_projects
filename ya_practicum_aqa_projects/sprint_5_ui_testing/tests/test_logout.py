import data
from locators import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogout:
    def test_logout(self, driver):
        driver.get(data.TestUrls.LOGIN_PAGE)
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(data.TestCredentials.EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(data.TestCredentials.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.PERSONAL_ACC_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.LOGOUT_BUTTON)
        )

        driver.find_element(*Locators.LOGOUT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON)
        )

        assert data.TestUrls.LOGIN_PAGE == driver.current_url
        assert driver.find_element(*Locators.LOGIN_BUTTON).text == "Войти"
