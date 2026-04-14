# pages/order_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators

    def fill_first_form(self, name, surname, address, metro_station, phone):
        self.input_text(self.locators.NAME_INPUT, name)
        self.input_text(self.locators.SURNAME_INPUT, surname)
        self.input_text(self.locators.ADDRESS_INPUT, address)

        metro_input = self.find_element(self.locators.METRO_STATION_INPUT)
        metro_input.click()
        metro_input.send_keys(metro_station)
        station_option = self.wait.until(
            EC.element_to_be_clickable(self.locators.METRO_STATION_SELECT)
        )
        station_option.click()

        self.input_text(self.locators.PHONE_INPUT, phone)
        self.click_element(self.locators.NEXT_BUTTON)

    def fill_second_form(self, delivery_date, rental_period, color=None, comment=""):
        date_input = self.find_element(self.locators.DELIVERY_DATE_INPUT)
        date_input.click()
        date_input.send_keys(delivery_date)
        date_input.send_keys(Keys.ENTER)
        self.wait.until(EC.element_to_be_clickable(self.locators.DELIVERY_DATE_INPUT))

        self.click_element(self.locators.RENTAL_PERIOD_DROPDOWN)
        period_locator = (
            By.XPATH,
            self.locators.RENTAL_PERIOD_OPTION_TEMPLATE.format(rental_period)
        )
        self.click_element(period_locator)

        if color == "black":
            self.click_element(self.locators.COLOR_BLACK)
        elif color == "grey":
            self.click_element(self.locators.COLOR_GREY)

        if comment:
            self.input_text(self.locators.COMMENT_INPUT, comment)

        order_button = self.find_element(self.locators.FINAL_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", order_button)
        self.click_element(self.locators.FINAL_ORDER_BUTTON)

    def confirm_order(self):
        self.click_element(self.locators.CONFIRM_YES_BUTTON)

    def is_success_modal_displayed(self):
        return self.find_element(self.locators.SUCCESS_MODAL).is_displayed()

    def get_success_message(self):
        return self.get_text(self.locators.SUCCESS_MESSAGE)