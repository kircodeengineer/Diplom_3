import allure
from selenium import webdriver

@allure.step('Настройка драйвера браузера {browser}')
def setup_driver(browser):
    if browser == 'chrome':
        return webdriver.Chrome()
    elif browser == 'firefox':
        return webdriver.Firefox()