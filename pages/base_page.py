import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains


class BasePage:
    @allure.step('Инициализация класса')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие {url}')
    def _open_page(self, url):
        self.driver.get(url)
        WebDriverWait(self.driver, 15).until(expected_conditions.url_to_be(url))

    @allure.step('Клик по локатору {locator}')
    def _click_locator(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(locator))
        locator_to_click = self.driver.find_element(*locator)
        locator_to_click.click()

    @allure.step('Ввод {keys} по локатору {locator}')
    def _send_keys_by_locator(self, locator, keys):
        element = self.driver.find_element(*locator)
        element.send_keys(keys)

    @allure.step('Присутствует ли элемент по локатору {locator}')
    def _is_element_exist_by_locator(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located(locator))
        element = self.driver.find_element(*locator)
        return element.is_displayed()

    @allure.step('Получить текст по локатору {locator}')
    def _get_text_by_locator(self, locator):
        element = self.driver.find_element(*locator)
        return element.text

    @allure.step('Ожидать загрузку страницы {url}')
    def _wait_page_load(self, url):
        WebDriverWait(self.driver, 15).until(expected_conditions.url_to_be(url))

    @allure.step('Ожидать прогрузки всех элементов по локатору {locator}')
    def _wait_presence_of_all_elements_located(self, locator):
        return WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_all_elements_located(locator))

    @allure.step('Ожидать прогрузки элемента по локатору {locator}')
    def _wait_presence_of_element_located(self, locator):
        return WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located(locator))

    @allure.step('Ожидать отображения элемента по локатору {locator}')
    def _wait_visibility_of_element_located(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидать скрытия элемента по локатору {locator}')
    def _wait_invisibility_of_element_located(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step('Ожидать отсутствия текста у элемента по локатору {locator}')
    def _wait_text_not_to_be_present_in_element(self, locator, text):
        WebDriverWait(self.driver, 30).until_not(expected_conditions.text_to_be_present_in_element(locator, text))

    @allure.step('Ожидать кликабельности элемента по локатору {locator}')
    def _wait_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(locator))

    def _drag_and_drop(self, what_locator, where_locator):
        self._wait_element_to_be_clickable(what_locator)
        what = self.driver.find_element(*what_locator)
        where = self.driver.find_element(*where_locator)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(what, where).perform()