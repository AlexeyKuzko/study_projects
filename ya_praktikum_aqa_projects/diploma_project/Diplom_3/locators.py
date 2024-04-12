from selenium.webdriver.common.by import By


class AccountPageLocators:
    LOGOUT_BUTTON = By.XPATH, '//*[contains(@class, "Account_button")]'
    ORDER_COMPLETED_TEXT = By.XPATH, '//p[text()="Выполнен"]'
    ORDER_HISTORY_LINK = By.XPATH, '//*[@href="/account/order-history"]'
    ORDER_NUMBER_IN_ORDER_HISTORY = By.XPATH, '//*[contains(@class,"textBox")]//p[contains(@class,"digits-default")]'
    PROFILE_LINK = By.XPATH, '//*[@href="/account/profile"]'


class BasePageLocators:
    ACCOUNT_LINK = By.XPATH, '//*[@href="/account"]'
    CLOSE_BUTTON = By.XPATH, '//button[contains(@class,"close")]'
    CONSTRUCTOR_LINK = By.XPATH, '//p[text()="Конструктор"]/parent::a'
    EMAIL_FIELD = By.XPATH, '//label[text()="Email"]/following-sibling::input'
    ORDER_FEED_LINK = By.XPATH, '//p[text()="Лента Заказов"]/parent::a'
    PASSWORD_FIELD = By.XPATH, '//input[@type="password"]'


class LoginPageLocators:
    ENTER_BUTTON = By.XPATH, '//button[text()="Войти"]'
    FORGOT_PASSWORD_LINK = By.XPATH, '//*[@href="/forgot-password"]'


class ConstructorPageLocators:
    CONSTRUCTOR_TITLE = By.XPATH, '//h1[text()="Соберите бургер"]'
    DEFAULT_ORDER_NUMBER = By.XPATH, '//h2[text()="9999"]'
    ENTER_ACCOUNT_BUTTON = By.XPATH, '//button[text()="Войти в аккаунт"]'
    INGREDIENT_BUN = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]'
    INGREDIENT_COUNTER = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]//p[contains(@class, "counter__num")]'
    INGREDIENT_DETAILS_MODAL = By.XPATH, '//*[@id="root"]/div/section/div[1]'
    INGREDIENT_DETAILS_TITLE = By.XPATH, '//h2[text()="Детали ингредиента"]'
    INGREDIENT_FILLING = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa77"]'
    INGREDIENT_SAUCE = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa74"]'
    ORDER_CART = By.XPATH, '//ul[contains(@class,"basket")]'
    ORDER_CREATE_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'
    ORDER_NUMBER_IN_CONSTRUCTOR = By.XPATH, '//*[contains(@class, "type_digits-large")]'
    ORDER_IS_PREPARING_TEXT = By.XPATH, '//p[text()="Ваш заказ начали готовить"]'


class OrderFeedPageLocators:
    ALL_ORDERS_COMPLETED_TEXT = By.XPATH, '//li[text()="Все текущие заказы готовы!"]'
    COMPLETE_ORDERS_COUNT_TODAY = By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class,"digits-large")]'
    COMPLETE_ORDERS_COUNT_TOTAL = By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class,"digits-large")]'
    ORDER_CONTENTS_TITLE = By.XPATH, '//p[text()="Cостав"]'
    ORDER_FEED_TITLE = By.XPATH, '//h1[text()="Лента заказов"]'
    ORDER_IN_FEED_LINK = By.XPATH, '//*[contains(@class, "OrderHistory_link")]'
    ORDER_NUMBER_IN_ORDER_FEED = By.XPATH, '//p[text()="{}"]'
    ORDER_NUMBER_IN_WORK = By.XPATH, '//*[contains(@class,"orderListReady")]//li[contains(@class,"digits-default")]'


class ResetPasswordPageLocators:
    RESET_BUTTON = By.XPATH, '//button[text()="Восстановить"]'
    SAVE_BUTTON = By.XPATH, '//button[text()="Сохранить"]'
    SHOW_PASSWORD_ICON = By.XPATH, '//div[contains(@class,"icon-action")]'
    PASSWORD_FIELD_ACTIVE = By.CSS_SELECTOR, '.input.input_status_active'
