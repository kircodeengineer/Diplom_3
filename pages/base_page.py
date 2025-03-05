from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _open_page(self, url):
        self.driver.get(url)
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(url))

    def _click_locator(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        locator_to_click = self.driver.find_element(*locator)
        locator_to_click.click()

    def _send_keys_by_locator(self, locator, keys):
        element = self.driver.find_element(*locator)
        element.send_keys(keys)

    def _is_element_exist_by_locator(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator))
        element = self.driver.find_element(*locator)
        return element.is_displayed()

    def _get_text_by_locator(self, locator):
        element = self.driver.find_element(*locator)
        return element.text