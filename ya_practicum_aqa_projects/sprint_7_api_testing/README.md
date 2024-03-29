# Sprint_7
## Проект автоматизации тестирования API сервиса [«Яндекс.Самокат»](https://qa-scooter.praktikum-services.ru/)
****
### Используемые технологии
- [Allure Report](https://allurereport.org/docs/gettingstarted-installation/)
- [pytest](https://pypi.org/project/pytest/)
- [allure-pytest](https://pypi.org/project/allure-pytest/)
- [requests](https://pypi.org/project/requests/)
****
### Запуск проекта

Загружаем архив с файлами проекта, распаковываем и открываем его в терминале

    pip install -r requirements.txt
    pytest -v ./tests  --alluredir=allure_results
    allure serve allure_results
****
### Структура проекта
##### Проект состоит из двух пакетов, двух вспомогательных модулей и директории с отчетами Allure
###### tests/ - пакет с модулями автотестов:
- test_courier_create.py - тесты создания курьера
- test_courier_login.py - тесты логина курьера
- test_order_create.py - тесты создания заказа
- test_order_list.py - тесты получения списка заказов

###### helpers/ - пакет с модулями, содержащими функции-помощники:
- api_client.py - модуль содержит 
`class BaseRequests` с базовыми методами взаимодействия с API, 
`class CourierRequests` c методами запросов к API связанными с операциями над курьерами и 
`class OrderApiClient` c методами запросов к API для создания заказа и получения списка заказов
- data.py - содержит `class Urls` с константами URL тестируемых ресурсов

###### вспомогательный модуль в корне проекта:
- conftest.py - содержит фикстуры pytest

###### директория allure_results:
- содержит сгенерированные отчеты Allure