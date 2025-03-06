import allure

from pages.main_page import MainPage
from pages.forgot_password_page import ForgotPasswordPage
import urls

class TestMainPage:
    @allure.title('Переход на Главную страницу по клику на кнопку Конструктор')
    def test_go_to_main_page_from_forgot_password_page_by_button_click(self, page_driver):
        forgot_password_page = ForgotPasswordPage(page_driver)
        forgot_password_page.open()
        forgot_password_page.click_constructor_button()
        current_url = page_driver.current_url
        assert current_url == urls.MAIN_PAGE

    @allure.title('Переход на страницу с лентой заказов по клику на кнопку Лента заказов')
    def test_go_to_feed_page_from_main_page_by_button_click(self, page_driver):
        main_page = MainPage(page_driver)
        main_page.open()
        main_page.click_orders_list_button()
        current_url = page_driver.current_url
        assert current_url == urls.FEED_PAGE

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_pop_up_ingredient_window_by_ingredient_click(self, page_driver):
        main_page = MainPage(page_driver)
        main_page.open()
        main_page.click_on_ingredient()
        assert main_page.is_ingredient_window_popped_up()

    @allure.title('Всплывающее окно с деталями закрывается кликом по крестику')
    def test_close_popped_up_ingredient_window_by_button_click(self, page_driver):
        main_page = MainPage(page_driver)
        main_page.open()
        main_page.click_on_ingredient()
        main_page.click_close_button()
        assert not main_page.is_ingredient_window_popped_up()

    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_increase_ingredient_counter(self, page_driver):
        main_page = MainPage(page_driver)
        main_page.open()
        prev_counter_value = main_page.get_count_value()
        main_page.add_buns_to_order()
        curr_counter_value = main_page.get_count_value()
        assert curr_counter_value > prev_counter_value

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_logged_in_user_can_make_order(self, logged_in_main_page_driver):
        main_page = MainPage(logged_in_main_page_driver)
        main_page.open()
        main_page.add_buns_to_order()
        main_page.click_make_order_button()
        assert main_page.is_order_window_popped_up()
