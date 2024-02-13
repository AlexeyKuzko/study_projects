# Sprint_5

## Проект автоматизации тестирования сервиса [Stellar Burgers](https://stellarburgers.nomoreparties.site/)

### Используемые технологии

- [pytest](https://docs.pytest.org/en/8.0.x/)
- [Selenium Web Driver 3.x](https://selenium.dev/)
- [Google Chrome](https://googlechromelabs.github.io/chrome-for-testing/)

### Тесты, которые удалось реализовать

#### Регистрация

##### Тестовые методы определены в `class TestRegister` модуля _test_register.py_

- Проверка успешной регистрации: `def test_register_positive_path()`. Поле «Имя» должно быть не пустым; в поле Email
  введён email в формате логин@домен: например, 123@ya.ru. Минимальный пароль — шесть символов.
- Проверка ошибки для некорректного пароля - `def test_register_negative_path()`.

#### Вход

##### Тестовые методы определены в `class TestLogin` модуля _test_login.py_

- Проверка входа по кнопке «Войти в аккаунт» на главной: `def test_login_from_main()`.
- Проверка входа через кнопку «Личный кабинет»: `def test_login_from_personal_acc()`.
- Проверка входа через кнопку в форме регистрации: `def test_login_from_register()`.
- Проверка входа через кнопку в форме восстановления пароля: `def test_login_from_reset_data.password()`.

#### Переход в личный кабинет

##### Тестовый метод определен в `class TestGoToPersonalAccount` модуля _test_go_to_personal_acc.py_

- Проверка перехода по клику на «Личный кабинет»: `def test_go_to_personal_acc()`.

#### Переход из личного кабинета в конструктор

##### Тестовый метод определен в `class TestGoToConstructor` модуля _test_go_to_constructor.py_

- Проверка перехода по клику на «Конструктор»: `def test_go_from_personal_acc_to_constructor`.
- Проверка перехода по клику на логотип Stellar Burgers: `def test_go_from_personal_acc_to_constructor_by_logo`.

#### Выход из аккаунта

##### Тестовый метод определен в `class TestLogout` модуля _test_logout.py_

- Проверка выхода по кнопке «Выйти» в личном кабинете: `def test_logout()`.

#### Раздел «Конструктор»

##### Тестовые методы определены в `class TestConstructor` модуля _test_constructor.py_

- Проверка перехода к разделу "Булки": `def test_constructor_go_to_buns()`.
- Проверка перехода к разделу "Соусы": `def test_constructor_go_to_sauces()`.
- Проверка перехода к разделу "Начинки": `def test_constructor_go_to_toppings()`.