from selenium.webdriver.common.by import By


class BasePageLocators:
    important_questions_section = (By.XPATH, './/div[text() = "Вопросы о важном"]')
    cookie_consent_button = (By.XPATH, './/button[@class="App_CookieButton__3cvqF" and text() = "да все привыкли"]')
    header_booking_button = (By.XPATH, './/button[@class="Button_Button__ra12g" and text() = "Заказать"]')
    next_button = (By.XPATH, './/button[text() = "Далее"]')
    middle_booking_button = (By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text() = "Заказать"]',)
    scooter_logo = (By.XPATH, './/img[@alt="Scooter"]')
    yandex_logo = (By.XPATH, './/img[@alt="Yandex"]')
    logo_dzen = (By.XPATH, './/svg[@class="desktop-base-header__logoBrand-3W desktop-base-header__isMorda-mX"]')
    dzen_find_button = (By.XPATH, './/button[@type="submit" and text() = "Найти"]')
