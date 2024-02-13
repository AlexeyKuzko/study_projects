import pytest
import data
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(data.TestUrls.MAIN_PAGE)
    yield driver
    driver.quit()
