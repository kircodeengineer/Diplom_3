import pytest

from pages.main_page import  MainPage
from pages.feed_page import  FeedPage
from pages.account_profile_page import AccountProfilePage
from pages.account_order_history import AccountOrderHistoryPage
from locators.feed_page import *

class TestFeedPage:
    def test_pop_up_order_details_window_by_click_order_in_list(self, page_driver):
        main_page = MainPage(page_driver)
        main_page.open()
        main_page.click_orders_list_button()
        feed_page = FeedPage(page_driver)
        feed_page.click_order()
        assert feed_page.is_order_details_window_popped_up()

    def test_order_exist_in_user_order_history_and_in_order_in_list(self, logged_in_main_page_driver):
        main_page = MainPage(logged_in_main_page_driver)
        main_page.open()
        main_page.add_buns_to_order()
        main_page.click_make_order_button()
        order_number = main_page.get_order_number()
        main_page.close_order_popped_up_window()
        main_page.click_personal_account_href()
        account_profile_page = AccountProfilePage(logged_in_main_page_driver)
        account_profile_page.click_order_history_button()
        account_order_history = AccountOrderHistoryPage(logged_in_main_page_driver)
        is_order_number_found_in_user_order_history = account_order_history.is_order_number_found(order_number)
        feed_page = FeedPage(logged_in_main_page_driver)
        feed_page.open()
        is_order_number_found_in_feed = feed_page.is_order_number_found(order_number)
        assert is_order_number_found_in_user_order_history
        assert is_order_number_found_in_feed

    @pytest.mark.parametrize('counter_locator', [TOTAL_ORDER_COUNTER, DAILY_ORDER_COUNTER])
    def test_orders_counter_increase(self, logged_in_main_page_driver, counter_locator):
        feed_page = FeedPage(logged_in_main_page_driver)
        feed_page.open()
        prev_counter_value = feed_page.get_counter_by_locator(counter_locator)
        main_page = MainPage(logged_in_main_page_driver)
        main_page.open()
        main_page.add_buns_to_order()
        main_page.click_make_order_button()
        feed_page.open()
        current_counter_value = feed_page.get_counter_by_locator(counter_locator)
        assert current_counter_value > prev_counter_value