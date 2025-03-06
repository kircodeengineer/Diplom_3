import allure

import urls
from pages.base_page import BasePage
from locators.account_profile_page import *


class AccountProfilePage(BasePage):
    @allure.step('Нажать кнопку История заказов')
    def click_order_history_button(self):
        self._click_locator(ORDERS_HISTORY_BUTTON)
        self._wait_page_load(urls.ORDER_HISTORY_PAGE)

    @allure.step('Нажать кнопку закрывающую всплывающее окно')
    def click_exit_button(self):
        self._click_locator(EXIT_BUTTON)
        self._wait_page_load(urls.LOGIN_PAGE)
