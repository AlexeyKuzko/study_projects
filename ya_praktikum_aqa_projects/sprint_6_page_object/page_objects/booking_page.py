import allure
from page_objects.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from locators.booking_page_locators import BookingPageLocators


class BookingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Заполнение полей «Для кого самокат»')
    def fill_who_booking_scooter(self, first_name, surname, address, subway_station, mobile_number):
        self.find_page(BookingPageLocators.first_name_field).send_keys(first_name)
        self.find_page(BookingPageLocators.surname_field).send_keys(surname)
        self.find_page(BookingPageLocators.address_field).send_keys(address)
        self.click_page(BookingPageLocators.subway_station_field)
        self.find_page(BookingPageLocators.subway_station_field).send_keys(subway_station)
        self.wait_until_element_is_visible(BookingPageLocators.subway_station_choice)
        self.click_page(BookingPageLocators.subway_station_choice)
        self.find_page(BookingPageLocators.phone_field).send_keys(mobile_number)

    @allure.step('Нажать на кнопку Далее')
    def click_next_button(self):
        return self.click_page(BasePageLocators.next_button)

    @allure.step('Заполнение полей «Про аренду»')
    def fill_about_booking(self, comment):
        self.click_page(BookingPageLocators.datepicker_field)
        self.click_page(BookingPageLocators.datepicker)
        self.click_page(BookingPageLocators.time_of_lease_field)
        self.click_page(BookingPageLocators.time_of_lease_choice_one_day)
        self.click_page(BookingPageLocators.color_grey_field)
        self.find_page(BookingPageLocators.comment_field).send_keys(comment)

    @allure.step('Нажать кнопку Заказать')
    def click_finish_booking_button(self):
        return self.click_page(BookingPageLocators.booking_button)

    @allure.step('Нажать кнопку "Вы уверены? - Да"')
    def click_are_you_sure_yes_button(self):
        return self.click_page(BookingPageLocators.confidence_yes_button)

    @allure.step('Найти кнопку Посмотреть статус')
    def find_show_status_button(self):
        return self.find_page(BookingPageLocators.show_status_button)

    @allure.step('Кликнуть лого Яндекса')
    def click_yandex_logo(self):
        return self.click_page(BasePageLocators.yandex_logo)

    @allure.step('Кликнуть лого Самоката')
    def click_scooter_logo(self):
        return self.click_page(BasePageLocators.scooter_logo)
