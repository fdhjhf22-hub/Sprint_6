import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="function")
def driver():
    options = Options()
    # Разрешаем открытие новых вкладок без блокировки
    options.set_preference("dom.disable_beforeunload", False)
    options.set_preference("dom.disable_open_during_load", False)
    # При необходимости раскомментировать для запуска без GUI
    # options.add_argument("--headless")

    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()