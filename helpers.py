import allure
from selenium import webdriver
import requests

import api

@allure.step('Настройка драйвера браузера {browser}')
def setup_driver(browser):
    if browser == 'chrome':
        return webdriver.Chrome()
    elif browser == 'firefox':
        return webdriver.Firefox()

@allure.step('Регистрация пользователя с данными {user_data}')
def register_user(user_data):
    response = requests.post(f"{api.MAIN_URL}{api.CREATE_USER}", json=user_data)
    return response

@allure.step('Удаление пользователя с токеном')
def delete_user(access_token):
    headers = {"Authorization": access_token}
    requests.delete(f"{api.MAIN_URL}{api.DELETE_USER}", headers=headers)