import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators.reset_password_page import *
from pages.base_page import BasePage
import urls


class ResetPasswordPage(BasePage):
    @allure.step('Открыть страницу Восстановления пароля')
    def open(self):
        self._open_page(urls.RESET_PASSWORD_PAGE)

    @allure.step('Кликнуть по кнопке показать/скрыть пароль')
    def click_on_show_password_button(self):
        self._click_locator(SHOW_PASSWORD_BUTTON)
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(FIELD_PASSWORD_ACTIVE))

    @allure.step('Активно ли поле ввода пароля')
    def is_field_password_active(self):
        return self._is_element_exist_by_locator(FIELD_PASSWORD_ACTIVE)
