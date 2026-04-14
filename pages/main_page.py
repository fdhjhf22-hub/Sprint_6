from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators

    def click_order_button_top(self):
        self.click_element(self.locators.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        self.scroll_to_element(self.locators.ORDER_BUTTON_BOTTOM)
        self.click_element(self.locators.ORDER_BUTTON_BOTTOM)

    def scroll_to_faq_section(self):
        self.scroll_to_element(self.locators.FAQ_SECTION)

    def get_faq_questions_count(self):
        return len(self.find_elements(self.locators.FAQ_QUESTIONS))

    def click_question(self, index):
        questions = self.find_elements(self.locators.FAQ_QUESTIONS)
        if index >= len(questions):
            raise IndexError(f"Вопрос с индексом {index} не существует")
        self.scroll_into_view(questions[index])
        self.wait.until(EC.element_to_be_clickable(questions[index])).click()
        answers = self.find_elements(self.locators.FAQ_ANSWERS)
        self.wait.until(EC.visibility_of(answers[index]))

    def get_answer_text(self, index):
        answers = self.find_elements(self.locators.FAQ_ANSWERS)
        if index >= len(answers):
            raise IndexError(f"Ответ с индексом {index} не существует")
        return answers[index].text

    def click_scooter_logo(self):
        self.click_element(self.locators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(self.locators.YANDEX_LOGO)

    def accept_cookies_if_present(self):
        self.accept_cookies(self.locators.COOKIE_ACCEPT_BUTTON)