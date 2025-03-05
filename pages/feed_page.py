from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages.base_page import BasePage
from locators.feed_page import *
import urls

class FeedPage(BasePage):
    def open(self):
        self._open_page(urls.FEED_PAGE)

    def click_order(self):
        self._click_locator(TOP_ORDER_IN_LIST)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(ORDER_STRUCTURE))

    def is_order_details_window_popped_up(self):
        return self._is_element_exist_by_locator(ORDER_STRUCTURE)

    def is_order_number_found(self, order_number):
        elements = WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_all_elements_located(ORDERS))
        for element in elements:
            if order_number == element.text:
                return True
        return True

    def get_counter_by_locator(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located(locator))
        return int(self._get_text_by_locator(locator))

    def get_order_number_in_progress(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located(ORDER_NUMBER_IN_PROGRESS))
        return self._get_text_by_locator(ORDER_NUMBER_IN_PROGRESS)