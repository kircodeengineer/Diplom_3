from pages.main_page import MainPage
from pages.account_profile_page import AccountProfilePage
import urls

class TestAccountProfilePage:
    def test_go_to_account_profile_page_from_main_page_by_button_click(self, logged_in_main_page_driver):
        main_page = MainPage(logged_in_main_page_driver)
        main_page.click_personal_account_href()
        current_url = logged_in_main_page_driver.current_url
        assert current_url == urls.ACCOUNT_PAGE

    def test_go_to_order_history(self, logged_in_main_page_driver):
        main_page = MainPage(logged_in_main_page_driver)
        main_page.click_personal_account_href()
        account_profile_page = AccountProfilePage(logged_in_main_page_driver)
        account_profile_page.click_order_history_button()
        current_url = logged_in_main_page_driver.current_url
        assert current_url == urls.ORDER_HISTORY_PAGE