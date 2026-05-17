"""Pytest fixtures for Yandex Praktikum Automation QA projects: Sprint 5 UI Testing."""

import pytest
import data
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(data.TestUrls.MAIN_PAGE)
    yield driver
    driver.quit()
