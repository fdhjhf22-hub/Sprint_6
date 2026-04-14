import allure
import pytest
from pages.main_page import MainPage
from urls import MAIN_PAGE_URL, DZEN_URL
from data import FAQ_ANSWERS


class TestMainPage:

    @allure.title("Проверка перехода на главную страницу Самоката по клику на логотип")
    def test_scooter_logo_opens_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(MAIN_PAGE_URL)
        main_page.accept_cookies_if_present()
        main_page.click_scooter_logo()
        assert driver.current_url == MAIN_PAGE_URL

    @allure.title("Переход на страницу Дзена по клику на логотип Яндекса")
    def test_yandex_logo_opens_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(MAIN_PAGE_URL)
        main_page.accept_cookies_if_present()

        initial_windows = driver.window_handles
        main_page.click_yandex_logo()
        main_page.wait_for_new_window(initial_windows)
        main_page.switch_to_window(1)

        # Увеличиваем таймаут до 20 секунд, чтобы дождаться редиректа
        main_page.wait_for_url_contains("dzen.ru", timeout=20)

        current_url = main_page.get_current_url()
        assert "dzen.ru" in current_url or "yandex.ru" in current_url, \
            f"URL не содержит ожидаемых доменов: {current_url}"

    @allure.title("Проверка ответов на вопросы FAQ")
    @pytest.mark.parametrize("question_index, expected_answer", list(enumerate(FAQ_ANSWERS)))
    def test_faq_question_opens_correct_answer(self, driver, question_index, expected_answer):
        main_page = MainPage(driver)
        main_page.open_url(MAIN_PAGE_URL)
        main_page.accept_cookies_if_present()
        main_page.scroll_to_faq_section()

        assert main_page.get_faq_questions_count() == len(FAQ_ANSWERS)

        main_page.click_question(question_index)
        actual_answer = main_page.get_answer_text(question_index)

        assert expected_answer in actual_answer