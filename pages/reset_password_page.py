from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException

from locators.reset_password_page import *
from pages.base_page import BasePage
import urls


class ResetPasswordPage(BasePage):
    def open(self):
        self._open_page(urls.RESET_PASSWORD_PAGE)

    def click_on_show_password_button(self):
        self._click_locator(SHOW_PASSWORD_BUTTON)
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(FIELD_PASSWORD_ACTIVE))

    def is_field_password_active(self):
        return self._is_element_exist_by_locator(FIELD_PASSWORD_ACTIVE)
