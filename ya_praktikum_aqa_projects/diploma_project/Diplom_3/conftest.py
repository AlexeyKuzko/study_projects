import pytest
from selenium import webdriver

from data import Urls, UserHelper
from pages.login_page import LoginPage
from pages.constructor_page import ConstructorPage


@pytest.fixture(params=['chrome', 'firefox'])
def get_driver(request):
    if request.param == 'firefox':
        get_driver = webdriver.Firefox()
    elif request.param == 'chrome':
        get_driver = webdriver.Chrome()
    get_driver.get(Urls.BASE_URL)
    yield get_driver
    get_driver.quit()


@pytest.fixture(scope='session')
def create_user():
    return UserHelper.reg_user()


@pytest.fixture
def create_order(get_driver):
    constructor_page = ConstructorPage(get_driver)
    constructor_page.create_order()


@pytest.fixture
def login_user(get_driver, create_user):
    constructor_page = ConstructorPage(get_driver)
    constructor_page.press_enter_account_button()
    login_page = LoginPage(get_driver)
    login_page.fill_email_field(create_user['email'])
    login_page.fill_password_field(create_user['password'])
    login_page.press_enter_button()


@pytest.fixture
def gen_email():
    return UserHelper.generate_email()
