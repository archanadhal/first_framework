import pytest
from selenium.webdriver import Chrome
from time import sleep

@pytest.fixture()
def driver():
    driver = Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")
    sleep(3)
    yield driver
    driver.quit()