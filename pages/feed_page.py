from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages.base_page import BasePage
from locators.feed_page import *

class FeedPage(BasePage):
    def click_order(self):
        self._click_locator(TOP_ORDER_IN_LIST)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(ORDER_STRUCTURE))

    def is_order_details_window_popped_up(self):
        return self._is_element_exist_by_locator(ORDER_STRUCTURE)