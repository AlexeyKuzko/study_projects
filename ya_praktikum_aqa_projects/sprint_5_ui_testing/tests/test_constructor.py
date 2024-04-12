from locators import *


class TestConstructor:
    def test_constructor_go_to_buns(self, driver):
        driver.find_element(*Locators.TOPPINGS_BUTTON).click()
        driver.find_element(*Locators.BUNS_BUTTON).click()

        assert "current" in driver.find_element(*Locators.BUNS_BUTTON).get_attribute(
            "class"
        )

    def test_constructor_go_to_sauces(self, driver):
        driver.find_element(*Locators.SAUCES_BUTTON).click()

        assert "current" in driver.find_element(*Locators.SAUCES_BUTTON).get_attribute(
            "class"
        )

    def test_constructor_go_to_toppings(self, driver):
        driver.find_element(*Locators.TOPPINGS_BUTTON).click()

        assert "current" in driver.find_element(
            *Locators.TOPPINGS_BUTTON
        ).get_attribute("class")
