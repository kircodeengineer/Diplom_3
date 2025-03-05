from selenium.webdriver.common.by import By

TOP_ORDER_IN_LIST = (By.XPATH, ".//*[contains(@class, 'OrderHistory_link')]")
ORDER_STRUCTURE = (By.XPATH, ".//p[text()='Cостав']")
ORDERS = (By.XPATH, ".//div[@class='OrderHistory_textBox__3lgbs mb-6']//p[@class='text text_type_digits-default']")
TOTAL_ORDER_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
DAILY_ORDER_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")