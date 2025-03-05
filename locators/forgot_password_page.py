from selenium.webdriver.common.by import By


FIELD_EMAIL = (By.XPATH, ".//input[@class='text input__textfield text_type_main-default']")
RECOVERY_BUTTON = (By.XPATH, './/button[text()="Восстановить"]')
CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")