import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import MAIN_PAGE_URL
from data import ORDER_DATA


class TestOrderPage:

    @allure.title("Позитивный сценарий заказа самоката через верхнюю кнопку")
    @pytest.mark.parametrize(
        "name, surname, address, metro, phone, delivery_date, rental_period, color, comment",
        ORDER_DATA
    )
    def test_order_scooter_success_top_button(
        self, driver, name, surname, address, metro, phone,
        delivery_date, rental_period, color, comment
    ):
        main_page = MainPage(driver)
        with allure.step("Открыть главную страницу"):
            main_page.open_url(MAIN_PAGE_URL)
        with allure.step("Принять куки"):
            main_page.accept_cookies_if_present()
        with allure.step("Нажать кнопку Заказать вверху страницы"):
            main_page.click_order_button_top()

        order_page = OrderPage(driver)
        with allure.step("Заполнить первую форму заказа"):
            order_page.fill_first_form(name, surname, address, metro, phone)
        with allure.step("Заполнить вторую форму заказа"):
            order_page.fill_second_form(delivery_date, rental_period, color, comment)
        with allure.step("Подтвердить заказ"):
            order_page.confirm_order()
        with allure.step("Проверить появление сообщения об успешном заказе"):
            assert order_page.is_success_modal_displayed()
            assert "Заказ оформлен" in order_page.get_success_message()

    @allure.title("Позитивный сценарий заказа самоката через нижнюю кнопку")
    @pytest.mark.parametrize(
        "name, surname, address, metro, phone, delivery_date, rental_period, color, comment",
        ORDER_DATA
    )
    def test_order_scooter_success_bottom_button(
        self, driver, name, surname, address, metro, phone,
        delivery_date, rental_period, color, comment
    ):
        main_page = MainPage(driver)
        with allure.step("Открыть главную страницу"):
            main_page.open_url(MAIN_PAGE_URL)
        with allure.step("Принять куки"):
            main_page.accept_cookies_if_present()
        with allure.step("Нажать кнопку Заказать внизу страницы"):
            main_page.click_order_button_bottom()

        order_page = OrderPage(driver)
        with allure.step("Заполнить первую форму заказа"):
            order_page.fill_first_form(name, surname, address, metro, phone)
        with allure.step("Заполнить вторую форму заказа"):
            order_page.fill_second_form(delivery_date, rental_period, color, comment)
        with allure.step("Подтвердить заказ"):
            order_page.confirm_order()
        with allure.step("Проверить появление сообщения об успешном заказе"):
            assert order_page.is_success_modal_displayed()
            assert "Заказ оформлен" in order_page.get_success_message()