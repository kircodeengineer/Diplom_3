from pages.main_page import MainPage
import urls

class TestMainPage:

    #2
    def test_go_to_feed_page_from_main_page_by_button_click(self, page_driver):
        main_page = MainPage(page_driver)
        main_page.open()
        main_page.click_orders_list_button()
        current_url = page_driver.current_url
        assert current_url == urls.FEED_PAGE