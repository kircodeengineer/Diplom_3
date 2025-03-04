import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



@pytest.fixture(params=['chrome', 'firefox'])
def page_driver(request):
    driver = None
    if request.param == 'chrome':
        browser_options = webdriver.ChromeOptions()
        browser_options.add_argument('--headless')
        driver = webdriver.Chrome(options=browser_options)
    elif request.param == 'firefox':
        browser_options = webdriver.FirefoxOptions()
        browser_options.add_argument('--headless')
        driver = webdriver.Firefox(options=browser_options)
    yield driver
    driver.quit()
