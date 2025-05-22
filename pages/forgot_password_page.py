import allure

from pages.base_page import BasePage
from locators.forgot_password_page import *
import urls


class ForgotPasswordPage(BasePage):
    @allure.step('Открыть страницу Восстановления пароля')
    def open(self):
        self._open_page(urls.FORGOT_PASSWORD_PAGE)

    @allure.step('Ввести почту {email} в форму')
    def set_email(self, email):
        self._send_keys_by_locator(FIELD_EMAIL, email)

    @allure.step('Кликнуть по кнопке Восстановить')
    def click_recovery_button(self):
        self._click_locator(RECOVERY_BUTTON)
        self._wait_page_load(urls.RESET_PASSWORD_PAGE)

    @allure.step('Кликнуть по кнопке Конструктор')
    def click_constructor_button(self):
        self._click_locator(CONSTRUCTOR_BUTTON)
        self._wait_page_load(urls.MAIN_PAGE)