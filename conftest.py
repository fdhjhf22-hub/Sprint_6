import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.set_preference("dom.disable_beforeunload", False)
    options.set_preference("dom.disable_open_during_load", False)
    # options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()