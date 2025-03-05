from pages.main_page import  MainPage
from pages.feed_page import  FeedPage

import time

class TestFeedPage:
    def test_pop_up_order_details_window_by_click_order_in_list(self, page_driver):
        main_page = MainPage(page_driver)
        main_page.open()
        main_page.click_orders_list_button()
        feed_page = FeedPage(page_driver)
        feed_page.click_order()
        assert feed_page.is_order_details_window_popped_up()