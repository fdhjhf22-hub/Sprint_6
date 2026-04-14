import allure
import pytest
from pages.main_page import MainPage
from urls import MAIN_PAGE_URL
from data import FAQ_ANSWERS


class TestMainPage:

    @allure.title("Проверка перехода на главную страницу Самоката по клику на логотип")
    def test_scooter_logo_opens_main_page(self, driver):
        main_page = MainPage(driver)
        with allure.step("Открыть главную страницу"):
            main_page.open_url(MAIN_PAGE_URL)
        with allure.step("Принять куки"):
            main_page.accept_cookies_if_present()
        with allure.step("Кликнуть на логотип Самоката"):
            main_page.click_scooter_logo()
        with allure.step("Проверить, что URL остался главной страницы"):
            assert main_page.get_current_url() == MAIN_PAGE_URL

    @allure.title("Переход на страницу Дзена по клику на логотип Яндекса")
    def test_yandex_logo_opens_dzen(self, driver):
        main_page = MainPage(driver)
        with allure.step("Открыть главную страницу"):
            main_page.open_url(MAIN_PAGE_URL)
        with allure.step("Принять куки"):
            main_page.accept_cookies_if_present()
        with allure.step("Сохранить список открытых вкладок"):
            initial_windows = main_page.get_window_handles()
        with allure.step("Кликнуть на логотип Яндекса"):
            main_page.click_yandex_logo()
        with allure.step("Дождаться открытия новой вкладки"):
            main_page.wait_for_new_window(initial_windows)
        with allure.step("Переключиться на новую вкладку"):
            main_page.switch_to_window(1)
        with allure.step("Дождаться загрузки страницы Дзена"):
            main_page.wait_for_url_contains("dzen.ru", timeout=20)

    @allure.title("Проверка ответов на вопросы FAQ")
    @pytest.mark.parametrize("question_index, expected_answer", list(enumerate(FAQ_ANSWERS)))
    def test_faq_question_opens_correct_answer(self, driver, question_index, expected_answer):
        main_page = MainPage(driver)
        with allure.step("Открыть главную страницу"):
            main_page.open_url(MAIN_PAGE_URL)
        with allure.step("Принять куки"):
            main_page.accept_cookies_if_present()
        with allure.step("Прокрутить до раздела FAQ"):
            main_page.scroll_to_faq_section()
        with allure.step(f"Кликнуть на вопрос №{question_index}"):
            main_page.click_question(question_index)
        with allure.step("Получить текст ответа"):
            actual_answer = main_page.get_answer_text(question_index)
        with allure.step("Проверить соответствие текста"):
            assert expected_answer in actual_answer