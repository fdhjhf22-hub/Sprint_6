import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import MAIN_PAGE_URL
from data import ORDER_DATA


class TestOrderPage:

    @allure.title("Позитивный сценарий заказа самоката")
    @pytest.mark.parametrize(
        "name, surname, address, metro, phone, delivery_date, rental_period, color, comment",
        ORDER_DATA
    )
    def test_order_scooter_success(
        self, driver, name, surname, address, metro, phone,
        delivery_date, rental_period, color, comment
    ):
        main_page = MainPage(driver)
        main_page.open_url(MAIN_PAGE_URL)
        main_page.accept_cookies_if_present()

        # Чередуем точки входа: для первого набора — верхняя кнопка, для второго — нижняя
        if name == ORDER_DATA[0][0]:
            main_page.click_order_button_top()
        else:
            main_page.click_order_button_bottom()

        order_page = OrderPage(driver)
        order_page.fill_first_form(name, surname, address, metro, phone)
        order_page.fill_second_form(delivery_date, rental_period, color, comment)
        order_page.confirm_order()

        assert order_page.is_success_modal_displayed()
        success_text = order_page.get_success_message()
        assert "Заказ оформлен" in success_text