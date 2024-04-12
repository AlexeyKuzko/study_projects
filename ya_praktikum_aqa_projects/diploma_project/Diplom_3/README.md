## Дипломный проект. Задание 3: веб-приложение

### Автотесты для проверки [веб-приложения Stellar Burgers](https://stellarburgers.nomoreparties.site/)

### Реализованные сценарии

С помощью паттерна Page Object Model, созданы тесты, покрывающие функциональность `Восстановление пароля`, 
`Личный кабинет`, `Проверка основного функционала`, `Раздел «Лента заказов»`

Отчет Allure: `allure_results`

### Структура проекта

- `pages` - пакет, содержащий Page Object. Для каждой страницы создан отдельный класс с Page Object.
Например, `reset_password_page.py`, `account_page.py` и т.д.
- `tests` - пакет, содержащий тесты, разделенные по классам. Тесты разделены по тематике или функциональности.
Например, `test_reset_password.py`, `test_account.py` и т.д.
- `conftest.py` - модуль, содержащий фикстуры, используемые в тестах.
- `data.py` - модуль, содержащий вспомогательные данные и методы, используемые в тестах.
- `locators.py` - модуль, содержащий локаторы, используемые в тестах.

### Запуск автотестов

1. **Установка браузеров**

- [Google Chrome](https://www.google.com/chrome/)
- [Mozilla Firefox](https://www.mozilla.org/firefox/)

2. **Установка зависимостей**

    ```bash
    pip install -r requirements.txt
    ```

3. **Запуск автотестов и создание Allure-отчета**

    ```bash
    pytest -v tests --alluredir allure_results && allure serve allure_results
    ```
