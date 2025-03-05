from pages.main_page import MainPage
from pages.forgot_password_page import ForgotPasswordPage
import urls

class TestMainPage:
    def test_go_to_main_page_from_forgot_password_page_by_button_click(self, page_driver):
        forgot_password_page = ForgotPasswordPage(page_driver)
        forgot_password_page.open()
        forgot_password_page.click_constructor_button()
        current_url = page_driver.current_url
        assert current_url == urls.MAIN_PAGE

    def test_go_to_feed_page_from_main_page_by_button_click(self, page_driver):
        main_page = MainPage(page_driver)
        main_page.open()
        main_page.click_orders_list_button()
        current_url = page_driver.current_url
        assert current_url == urls.FEED_PAGE

    def test_popup_window_of_ingredient_by_ingredient_click(self, pages):
        pages.click_on_ingredient()
        actually_text = pages.check_show_window_with_details()
        assert actually_text == "Детали ингредиента"