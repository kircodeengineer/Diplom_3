from selenium.webdriver.common.by import By


REGISTRATION_BUTTON = (By.CSS_SELECTOR, ".button_button_size_medium__3zxIa")
REGISTRATION_PASS_ERROR = (By.CSS_SELECTOR, ".input__error.text_type_main-default")
EMAIL_FIELD = (By.XPATH, "(.//div[@class='input pr-6 pl-6 input_type_text input_size_default'])[2]/input")
NAME_FIELD = (By.XPATH, "(.//div[@class='input pr-6 pl-6 input_type_text input_size_default'])[1]/input")
PASS_FIELD = (By.XPATH, ".//input[@type='password' and @name='Пароль']")
ENTER_HREF = (By.XPATH, ".//a[@class='Auth_link__1fOlj' and @href='/login']")