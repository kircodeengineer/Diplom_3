from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages.base_page import BasePage
from locators.login_page import RECOVER_PASS_HREF
import urls

class LoginPage(BasePage):
    def open(self):
        self._open_page(urls.LOGIN_PAGE)

    def click_password_recovery_href(self):
        self._click_locator(RECOVER_PASS_HREF)
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(urls.FORGOT_PASSWORD_PAGE))