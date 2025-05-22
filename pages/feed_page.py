import allure

from pages.base_page import BasePage
from locators.feed_page import *
import urls


class FeedPage(BasePage):
    @allure.step('Открыть страницу Ленты заказов')
    def open(self):
        self._open_page(urls.FEED_PAGE)

    @allure.step('Клик по верхнему заказу Ленты заказов')
    def click_order(self):
        self._click_locator(TOP_ORDER_IN_LIST)
        self._wait_visibility_of_element_located(ORDER_STRUCTURE)

    @allure.step('Появилось ли всплывающее окно с деталями заказа')
    def is_order_details_window_popped_up(self):
        return self._is_element_exist_by_locator(ORDER_STRUCTURE)

    @allure.step('Найден ли номер заказа {order_number}')
    def is_order_number_found(self, order_number):
        elements = self._wait_presence_of_all_elements_located(ORDERS)
        for element in elements:
            if order_number in element.text:
                return True
        return False

    @allure.step('Получить счётчик по локатору {locator}')
    def get_counter_by_locator(self, locator):
        self._wait_presence_of_element_located(locator)
        return int(self._get_text_by_locator(locator))

    @allure.step('Получить номера заказа в работе')
    def get_order_number_in_progress(self):
        self._wait_presence_of_element_located(ORDER_NUMBER_IN_PROGRESS)
        return self._get_text_by_locator(ORDER_NUMBER_IN_PROGRESS)