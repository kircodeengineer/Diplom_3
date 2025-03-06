import allure

from pages.base_page import BasePage
from locators.account_order_history import *


class AccountOrderHistoryPage(BasePage):
    @allure.step('Присутствует ли номер заказа {order_number}')
    def is_order_number_found(self, order_number):
        elements = self._wait_presence_of_all_elements_located(ORDERS)
        for element in elements:
            if order_number in element.text:
                return True
        return False