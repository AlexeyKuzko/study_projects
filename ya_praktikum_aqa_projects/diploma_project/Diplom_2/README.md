## Дипломный проект. Задание 2: API

### Автотесты для проверки ручек API [Stellar Burgers](https://stellarburgers.nomoreparties.site/)

### Реализованные сценарии

Созданы тесты [API](https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/api-documentation.pdf?etag=3403196b527ca03259bfd0cb41163a89), 
покрывающие сценарии `Создание пользователя`, `Логин пользователя`, `Изменение данных пользователя`,`Создание заказа`, 
`Получение заказов конкретного пользователя`

Отчет Allure: `allure_results`

### Структура проекта

- `tests` - пакет, содержащий тесты, разделенные по классам. Для каждого эндпоинта тесты лежат в отдельном классе.
Например, `test_user_create.py`, `test_order_create.py` и т.д.
- `conftest.py` - модуль, содержащий фикстуры, используемые в тестах.
- `data.py` - модуль, содержащий вспомогательные данные и методы, используемые в тестах.

### Запуск автотестов

1. **Установка зависимостей**

    ```bash
     pip install -r requirements.txt
    ```

2. **Запуск автотестов и создание Allure-отчета**

    ```bash
    pytest -v tests --alluredir allure_results && allure serve allure_results
    ```
