from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.scroll_into_view(element)

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def get_text(self, locator):
        return self.find_element(locator).text

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_current_url(self):
        return self.driver.current_url

    def get_window_handles(self):
        return self.driver.window_handles

    def switch_to_window(self, index):
        windows = self.driver.window_handles
        if index < len(windows):
            self.driver.switch_to.window(windows[index])
        else:
            raise IndexError(f"Окно с индексом {index} не найдено")

    def wait_for_new_window(self, initial_handles, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > len(initial_handles)
        )

    def wait_for_url_contains(self, text, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: text in d.current_url
            )
        except TimeoutException:
            raise AssertionError(f"URL не содержит '{text}' через {timeout} сек.")

    def accept_cookies(self, locator):
        try:
            cookie_button = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(locator)
            )
            cookie_button.click()
        except TimeoutException:
            pass