from selenium.webdriver.common.by import By


class BookingPageLocators:
    header_booking_button = (By.XPATH, './/button[@class="Button_Button__ra12g" and text() = "Заказать"]')
    first_name_field = (By.XPATH, './/input[@placeholder="* Имя"]')
    surname_field = (By.XPATH, './/input[@placeholder="* Фамилия"]')
    address_field = (By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]')
    subway_station_field = (By.XPATH, './/input[@placeholder="* Станция метро"]')
    subway_station_choice = (By.XPATH, './/div[@class="select-search__select"]')
    phone_field = (By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]')
    datepicker_field = (By.XPATH, './/input[@placeholder="* Когда привезти самокат"]')
    datepicker = (By.XPATH, './/div[@class="react-datepicker__day react-datepicker__day--001 react-datepicker__day--outside-month"]')
    time_of_lease_field = (By.XPATH, './/div[@class="Dropdown-placeholder" and text() = "* Срок аренды"]')
    time_of_lease_choice_one_day = (By.XPATH, './/div[text() = "сутки"]')
    time_of_lease_choice_two_days = (By.XPATH, './/div[text() = "сутки"]')
    color_choice_field = (By.XPATH, './/div[@class="Order_Title__3EKne" and text() = "Цвет самоката"]')
    color_black_field = (By.XPATH, './/label[text() = "чёрный жемчуг"]')
    color_grey_field = (By.XPATH, './/label[text() = "серая безысходность"]')
    comment_field = (By.XPATH, './/input[@placeholder="Комментарий для курьера"]')
    booking_button = (By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text() = "Заказать"]')
    confidence_yes_button = (By.XPATH, './/button[text() = "Да"]')
    show_status_button = (By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text() = "Посмотреть статус"]')
