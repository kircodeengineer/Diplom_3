import allure
import pytest
from faker import Faker
import requests

import api
from pages.login_page import LoginPage
from setup_driver import setup_driver
from selenium.common.exceptions import ElementClickInterceptedException

@allure.step('Настройка драйвера браузера без регистрации пользователя {request}')
@pytest.fixture(params=['chrome', 'chrome'])
def page_driver(request):
    driver = setup_driver(request.param)
    yield driver
    driver.quit()

@allure.step('Регистрация пользователя с данными {user_data}')
def register_user(user_data):
    response = requests.post(f"{api.MAIN_URL}{api.CREATE_USER}", json=user_data)
    return response

@allure.step('Удаление пользователя с токеном')
def delete_user(access_token):
    headers = {"Authorization": access_token}
    requests.delete(f"{api.MAIN_URL}{api.DELETE_USER}", headers=headers)

@allure.step('Настройка драйвера браузера с регистрацией пользователя {request}')
@pytest.fixture(params=['chrome', 'firefox'])
def logged_in_main_page_driver(request):
    faker = Faker()
    user_data = None
    access_token = None
    status_code = 0
    timeout = 10
    while status_code != 200:
        user_data = {
            "email": faker.email(),
            "password": faker.password(),
            "name": faker.name()
        }
        response = register_user(user_data)
        access_token = response.json().get("accessToken")
        status_code = response.status_code
        timeout -= 1
        if timeout == 0:
            assert False, "Не удалось создать пользователя"

    driver = setup_driver(request.param)

    login_page = LoginPage(driver)
    login_page.open()
    try:
        login_page.enter_email_password(user_data["email"], user_data["password"])
        login_page.click_enter_button()
    except ElementClickInterceptedException as e:
        delete_user(access_token)
        driver.quit()
        assert False, e
    yield driver
    delete_user(access_token)
    driver.quit()