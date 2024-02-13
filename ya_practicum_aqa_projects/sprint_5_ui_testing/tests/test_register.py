import data
from locators import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegister:
    def test_register_positive_path(self, driver):
        driver.get(data.TestUrls.REG_PAGE)

        driver.find_element(*Locators.REG_NAME_INPUT).send_keys(data.TestCredentials.NAME)
        driver.find_element(*Locators.REG_EMAIL_INPUT).send_keys(data.TestCredentials.EMAIL)
        driver.find_element(*Locators.REG_PASSWORD_INPUT).send_keys(data.TestCredentials.PASSWORD)
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON)
        )

        assert data.TestUrls.LOGIN_PAGE == driver.current_url

    def test_register_negative_path(self, driver):
        driver.get(data.TestUrls.REG_PAGE)

        driver.find_element(*Locators.REG_NAME_INPUT).send_keys(data.TestCredentials.NAME)
        driver.find_element(*Locators.REG_EMAIL_INPUT).send_keys(data.TestCredentials.EMAIL)
        driver.find_element(*Locators.REG_PASSWORD_INPUT).send_keys(data.TestCredentials.bad_password())
        driver.find_element(*Locators.REG_BUTTON).click()

        assert (
            driver.find_element(*Locators.WRONG_PASSWORD_ERROR).text
            == "Некорректный пароль"
        )
