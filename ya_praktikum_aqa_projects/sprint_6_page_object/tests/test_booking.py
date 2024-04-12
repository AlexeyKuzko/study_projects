import allure
import pytest
from data import Urls
from page_objects.booking_page import BookingPage
from locators.base_page_locators import BasePageLocators
from locators.booking_page_locators import BookingPageLocators


class TestBookingPositive:

    @allure.title("Нажать кнопку «Заказать» (header)")
    @allure.description("Проверка открытия формы заказа по нажатию на кнопку «Заказать» в хэдере")
    def test_click_booking_header(self, driver):
        redirect_page = BookingPage(driver)
        redirect_page.open_base_url()
        redirect_page.click_header_booking_button()
        redirect_page.wait_until_element_is_visible(BasePageLocators.next_button)

        assert redirect_page.show_current_url() == Urls.ORDER_PAGE_URL

    @allure.title("Нажать кнопку «Заказать» (middle)")
    @allure.description("Проверка открытия формы заказа по нажатию на кнопку «Заказать» в середине страницы")
    def test_click_booking_middle(self, driver):
        redirect_page = BookingPage(driver)
        redirect_page.open_base_url()
        redirect_page.click_header_booking_button()
        redirect_page.wait_until_element_is_visible(BasePageLocators.next_button)

        assert redirect_page.show_current_url() == Urls.ORDER_PAGE_URL

    @allure.title("Заполнение формы оформления заказа (positive scenario)")
    @allure.description("Проверка создания заказа при вводе валидных данных (2 набора) в форме оформления заказа")
    @pytest.mark.parametrize(
        "first_name, surname, address, subway_station, mobile_number, comment",
        [
            [
                "Иван",
                "Петров",
                "Пушкина 1",
                "Новогиреево",
                "+79123456789",
                "Комментарий комментарий",
            ],
            [
                "Петр",
                "Иванов",
                "Колотушкина 2",
                "Новокосино",
                "+79876543210",
                "комментарий Комментарий",
            ],
        ],
    )
    def test_booking_form(self, driver, first_name, surname, address, subway_station, mobile_number, comment):
        booking_page = BookingPage(driver)
        booking_page.open_base_url()
        booking_page.click_header_booking_button()
        booking_page.click_cookie_consent()
        booking_page.fill_who_booking_scooter(first_name, surname, address, subway_station, mobile_number)
        booking_page.click_next_button()
        booking_page.fill_about_booking(comment)
        booking_page.click_finish_booking_button()
        booking_page.wait_until_element_is_clickable(BookingPageLocators.confidence_yes_button)
        booking_page.click_are_you_sure_yes_button()
        assert booking_page.find_show_status_button().text == "Посмотреть статус"

    @allure.title("Клик на лого Самоката")
    @allure.description(
        "Проверка редиректа на главную по нажатию на лого Самоката"
    )
    def test_redirect_scooter(self, driver):
        redirect_page = BookingPage(driver)
        redirect_page.open_base_url()
        redirect_page.click_header_booking_button()
        redirect_page.click_scooter_logo()
        redirect_page.wait_until_element_is_visible(BasePageLocators.middle_booking_button)
        assert redirect_page.show_current_url() == Urls.BASE_URL

    @allure.title("Клик на лого Яндекса")
    @allure.description(
        "Проверка редиректа на Дзен по нажатию на лого Яндекса"
    )
    def test_redirect_yandex(self, driver):
        redirect_page = BookingPage(driver)
        redirect_page.open_base_url()
        redirect_page.click_header_booking_button()
        assert len(driver.window_handles) == 1
        redirect_page.click_yandex_logo()
        redirect_page.check_window()
        redirect_page.wait_until_element_is_clickable(BasePageLocators.dzen_find_button)
        assert redirect_page.show_current_url() == Urls.REDIRECT_URL
