# Sprint_6
## Проект автоматизации тестирования сервиса [«Яндекс.Самокат»](https://qa-scooter.praktikum-services.ru/)
****
### Используемые технологии
- [pytest](https://docs.pytest.org/)
- [Selenium Web Driver 3.x](https://selenium.dev/)
- [Allure Report](https://allurereport.org)
- [Mozilla Firefox](https://www.mozilla.org/firefox/)
****
### Структура проекта
##### Проект состоит из трёх пакетов и директории с отчетами Allure
1. Пакет **tests** содержит модули с автоматизированными тестовыми сценариями
- test_questions.py - содержит `class TestImportantQuestions` с методом `def test_check_answers`, осуществляющим поочередную проверку элементов выпадающего списка «Вопросы о важном»
- test_booking.py - содержит `class TestBookingPositive` с методами, проверяющими полный путь позитивного сценария заказа самоката:
`def test_click_order_header` и `def test_click_order_middle` нажимают кнопку «Заказать» из хэдера и середины страницы, 
`def test_booking_form` заполняет форму заказа двумя наборами валидных данных и проверяет появление всплывающего окна с сообщением об успешном создании заказа, 
`def test_redirect_scooter` нажимает на логотип «Самоката» и проверяет попадание на главную страницу «Самоката», 
`def test_redirect_yandex` нажимает на логотип Яндекса и проверяет попадание на главную страницу Дзена
2. Пакет **page_objects** содержит page objects для тестируемых веб-страниц
- base_page.py - `class BasePage` с общими методами 
- booking_page.py - `class BookingPage` с методами страницы заказа самоката
- questions_page.py - `class ImportantQuestionsSection` с методами секции "Вопросы о важном"
3. Пакет **locators** содержит модули с локаторами элементов для соответствующих страниц
4. Директория **allure_results** содержит сгенерированные Allure-отчеты о результатах тестирования