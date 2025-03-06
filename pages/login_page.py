import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages.base_page import BasePage
from locators.login_page import *
import urls


class LoginPage(BasePage):
    @allure.step('Открыть страницу Логина')
    def open(self):
        self._open_page(urls.LOGIN_PAGE)

    @allure.step('Кликнуть по гиперссылке Восстановить пароль')
    def click_password_recovery_href(self):
        self._click_locator(RECOVER_PASS_HREF)
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(urls.FORGOT_PASSWORD_PAGE))

    @allure.step('Кликнуть по кнопке Войти')
    def click_enter_button(self):
        self._click_locator(ENTER_BUTTON)
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(urls.MAIN_PAGE))

    @allure.step('Ввести почту и пароль')
    def enter_email_password(self, email, password):
        self._send_keys_by_locator(EMAIL_FIELD, email)
        self._send_keys_by_locator(PASS_FIELD, password)