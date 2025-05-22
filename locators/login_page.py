from selenium.webdriver.common.by import By


RECOVER_PASS_HREF = (By.XPATH, ".//a[@class='Auth_link__1fOlj' and @href='/forgot-password']")
EMAIL_FIELD = (By.XPATH, "(.//fieldset[@class='Auth_fieldset__1QzWN mb-6'])//input[@name='name']")
PASS_FIELD = (By.XPATH, "(.//fieldset[@class='Auth_fieldset__1QzWN mb-6'])//input[@name='Пароль']")
ENTER_BUTTON = (By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text() ='Войти']")