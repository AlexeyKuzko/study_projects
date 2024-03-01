import allure
import pytest
from locators.questions_page_locators import QuestionsPageLocators
from page_objects.questions_page import ImportantQuestions


class TestQuestionsSection:

    answers = [
        "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
        "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
        "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
        "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
        "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
        "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
        "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
        "Да, обязательно. Всем самокатов! И Москве, и Московской области.",
    ]

    @allure.title("Тесты для раздела «Вопросы о важном»")
    @allure.step("Проверка, что когда нажимаешь на стрелочку, открывается ожидаемый текст ответа")
    @pytest.mark.parametrize("q, a, answers",
        [
            [
                QuestionsPageLocators.question_price,
                QuestionsPageLocators.answer_price,
                answers[0],
            ],
            [
                QuestionsPageLocators.question_need_several,
                QuestionsPageLocators.answer_need_several,
                answers[1],
            ],
            [
                QuestionsPageLocators.question_time_calculation,
                QuestionsPageLocators.answer_time_calculation,
                answers[2],
            ],
            [
                QuestionsPageLocators.question_book_for_today,
                QuestionsPageLocators.answer_book_for_today,
                answers[3],
            ],
            [
                QuestionsPageLocators.question_prolongation_and_return,
                QuestionsPageLocators.answer_prolongation_and_return,
                answers[4],
            ],
            [
                QuestionsPageLocators.question_charging_adapter,
                QuestionsPageLocators.answer_charging_adapter,
                answers[5],
            ],
            [
                QuestionsPageLocators.question_cancellation,
                QuestionsPageLocators.answer_cancellation,
                answers[6],
            ],
            [
                QuestionsPageLocators.question_delivery_to_suburbs,
                QuestionsPageLocators.answer_delivery_to_suburbs,
                answers[7],
            ],
        ],
    )
    def test_check_answers(self, driver, q, a, answers):
        questions_page = ImportantQuestions(driver)
        questions_page.open_base_url()
        questions_page.open_important_questions_section()
        questions_page.click_cookie_consent()
        questions_page.click_dropdown_menu_button(q)
        questions_page.wait_until_element_is_visible(a)

        assert questions_page.find_page(a).text == answers
