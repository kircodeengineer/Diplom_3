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

    def click_on_ingredient(self):
        self._click_locator(BUNS_INGREDIENT)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(INGREDIENT_DETAILS_POPUP))

    def is_ingredient_window_popped_up(self):
        return self._is_element_exist_by_locator(INGREDIENT_DETAILS_POPUP)

    def click_close_button(self):
        self._click_locator(CLOSE_BUTTON)
        WebDriverWait(self.driver, 5).until(expected_conditions.invisibility_of_element_located(INGREDIENT_DETAILS_POPUP))