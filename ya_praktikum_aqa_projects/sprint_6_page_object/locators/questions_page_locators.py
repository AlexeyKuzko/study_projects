from selenium.webdriver.common.by import By


class QuestionsPageLocators:
    question_price = (By.XPATH, './/div[text()="Сколько это стоит? И как оплатить?"]')
    answer_price = (
        By.XPATH,
        './/p[text()="Сутки — 400 рублей. Оплата курьеру — наличными или картой."]',
    )

    question_need_several = (
        By.XPATH,
        './/div[@class="accordion__button" and text()="Хочу сразу несколько самокатов! '
        'Так можно?"]',
    )
    answer_need_several = (
        By.XPATH,
        './/p[text()="Пока что у нас так: один заказ — один самокат. '
        "Если хотите покататься с друзьями, "
        'можете просто сделать несколько заказов — один за другим."]',
    )

    question_time_calculation = (
        By.XPATH,
        './/div[@class="accordion__button" and text()="Как рассчитывается время аренды?" ]',
    )
    answer_time_calculation = (
        By.XPATH,
        './/p[text()="Допустим, вы оформляете заказ на 8 мая. '
        "Мы привозим самокат 8 мая в течение дня. "
        "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. "
        'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."]',
    )

    question_book_for_today = (
        By.XPATH,
        './/div[@class="accordion__button" and text()="Можно ли заказать самокат прямо на сегодня?"]',
    )
    answer_book_for_today = (
        By.XPATH,
        './/p[text()="Только начиная с завтрашнего дня. Но скоро станем расторопнее."]',
    )

    question_prolongation_and_return = (
        By.XPATH,
        './/div[@class="accordion__button" and text()="Можно ли продлить заказ или вернуть самокат раньше?" ]',
    )
    answer_prolongation_and_return = (
        By.XPATH,
        './/p[text()="Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."]',
    )

    question_charging_adapter = (
        By.XPATH,
        './/div[@class="accordion__button" and text()="Вы привозите зарядку вместе с самокатом?"]',
    )
    answer_charging_adapter = (
        By.XPATH,
        './/p[text()="Самокат приезжает к вам с полной зарядкой. '
        "Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. "
        'Зарядка не понадобится."]',
    )

    question_cancellation = (
        By.XPATH,
        './/div[@class="accordion__button" and text()="Можно ли отменить заказ?"]',
    )
    answer_cancellation = (
        By.XPATH,
        './/p[text()="Да, пока самокат не привезли. '
        'Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."]',
    )

    question_delivery_to_suburbs = (
        By.XPATH,
        './/div[@class="accordion__button" and text()="Я жизу за МКАДом, привезёте?"]',
    )
    answer_delivery_to_suburbs = (
        By.XPATH,
        './/p[text()="Да, обязательно. Всем самокатов! И Москве, и Московской области."]',
    )
