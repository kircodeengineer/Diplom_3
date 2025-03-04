from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages.base_page import BasePage
from locators.forgot_password_page import *
import urls

class ForgotPasswordPage(BasePage):
    def open(self):
        self._open_page(urls.FORGOT_PASSWORD_PAGE)

    def set_email(self, email):
        self._send_keys_by_locator(FIELD_EMAIL, email)

    def click_recovery_button(self):
        self._click_locator(RECOVERY_BUTTON)
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(urls.RESET_PASSWORD_PAGE))