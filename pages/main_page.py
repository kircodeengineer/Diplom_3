import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains

from pages.base_page import BasePage
from locators.main_page import *
import urls


class MainPage(BasePage):
    @allure.step('Открыть Главную страницу')
    def open(self):
        self._open_page(urls.MAIN_PAGE)

    @allure.step('Кликнуть по гиперссылке Личный кабинет')
    def click_personal_account_href(self):
        self._click_locator(PERSONAL_ACCOUNT_HREF)
        self._wait_page_load(urls.ACCOUNT_PROFILE_PAGE)

    @allure.step('Кликнуть по кнопке Лента заказов')
    def click_orders_list_button(self):
        self._click_locator(ORDERS_LIST_BUTTON)
        self._wait_page_load(urls.FEED_PAGE)

    @allure.step('Кликнуть по ингредиенту')
    def click_on_ingredient(self):
        self._click_locator(BUNS_INGREDIENT)
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(INGREDIENT_DETAILS_POPUP))

    @allure.step('Присутствует ли ингредиент во всплывающем окне')
    def is_ingredient_window_popped_up(self):
        return self._is_element_exist_by_locator(INGREDIENT_DETAILS_POPUP)

    @allure.step('Кликнуть по кнопке закрывающей всплывающее окно')
    def click_close_button(self):
        self._click_locator(CLOSE_BUTTON)
        WebDriverWait(self.driver, 15).until(expected_conditions.invisibility_of_element_located(INGREDIENT_DETAILS_POPUP))

    @allure.step('Получить число позиций добавленного ингредиента')
    def get_count_value(self):
        return self._get_text_by_locator(INGREDIENT_COUNTER)

    @allure.step('Добавить булки в заказ')
    def add_buns_to_order(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(BUNS_INGREDIENT))
        buns = self.driver.find_element(*BUNS_INGREDIENT)
        order = self.driver.find_element(*ORDER)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(buns, order).perform()

    @allure.step('Кликнуть по кнопку Оформить заказ')
    def click_make_order_button(self):
        self._click_locator(MAKE_ORDER_BUTTON)
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(ORDER_DETAILS_POPUP))

    @allure.step('Всплыло ли окно с деталями заказа')
    def is_order_window_popped_up(self):
        return self._is_element_exist_by_locator(ORDER_DETAILS_POPUP)

    @allure.step('Получить номер заказа')
    def get_order_number(self):
        WebDriverWait(self.driver, 30).until_not(expected_conditions.text_to_be_present_in_element(ORDER_NUMBER, '9999'))
        return self._get_text_by_locator(ORDER_NUMBER)

    @allure.step('Закрыть всплывающее окно')
    def close_order_popped_up_window(self):
        self._click_locator(CLOSE_ORDER_POPPED_UP_WINDOW_BUTTON)
        WebDriverWait(self.driver, 15).until(expected_conditions.invisibility_of_element_located(ORDER_DETAILS_POPUP))