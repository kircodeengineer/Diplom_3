from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages.base_page import BasePage
from locators.main_page import *
import urls


class MainPage(BasePage):
    def open(self):
        self._open_page(urls.MAIN_PAGE)

    def click_personal_account_href(self):
        self._click_locator(PERSONAL_ACCOUNT_HREF)
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(urls.ACCOUNT_PROFILE_PAGE))

    def click_orders_list_button(self):
        self._click_locator(ORDERS_LIST_BUTTON)
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(urls.FEED_PAGE))