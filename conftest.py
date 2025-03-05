import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import requests

import urls
import locators.login_page
import api


def setup_driver(browser):
    if browser == 'chrome':
        return webdriver.Chrome()
    elif browser == 'firefox':
        return webdriver.Firefox()

@pytest.fixture(params=['chrome', 'firefox'])
def page_driver(request):
    driver = setup_driver(request.param)
    yield driver
    driver.quit()


def register_user(user_data):
    response = requests.post(f"{api.MAIN_URL}{api.CREATE_USER}", json=user_data)
    return response

def delete_user(access_token):
    headers = {"Authorization": access_token}
    requests.delete(f"{api.MAIN_URL}{api.DELETE_USER}", headers=headers)

@pytest.fixture(params=['chrome', 'firefox'])
def logged_in_main_page_driver(request):
    faker = Faker()
    status_code = 0
    user_data = None
    access_token = None
    while status_code != 200:
        user_data = {
            "email": faker.email(),
            "password": faker.password(),
            "name": faker.name()
        }
        response = register_user(user_data)
        access_token = response.json().get("accessToken")
        status_code = response.status_code
    try:
        driver = setup_driver(request.param)
        driver.get(urls.LOGIN_PAGE)
        WebDriverWait(driver, 15).until(expected_conditions.url_to_be(urls.LOGIN_PAGE))
        email_field = driver.find_element(*locators.login_page.EMAIL_FIELD)
        email_field.send_keys(user_data["email"])
        pass_field = driver.find_element(*locators.login_page.PASS_FIELD)
        pass_field.send_keys(user_data["password"])
        enter_button = driver.find_element(*locators.login_page.ENTER_BUTTON)
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(locators.login_page.ENTER_BUTTON))
        enter_button.click()
        WebDriverWait(driver, 15).until(expected_conditions.url_to_be(urls.MAIN_PAGE))
        yield driver
    except Exception as e:
        delete_user(access_token)
        assert False, e
    delete_user(access_token)
    driver.quit()