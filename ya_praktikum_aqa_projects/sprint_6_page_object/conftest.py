"""Pytest fixtures for Yandex Praktikum Automation QA projects: Sprint 6 Page Object."""

import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
