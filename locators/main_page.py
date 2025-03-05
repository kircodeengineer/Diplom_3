from selenium.webdriver.common.by import By


PERSONAL_ACCOUNT_HREF = (By.XPATH,".//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']")
ORDERS_LIST_BUTTON = (By.XPATH, ".//p[text()='Лента Заказов']")
BUNS_INGREDIENT = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
INGREDIENT_DETAILS_POPUP = (By.XPATH, '//h2[text()="Детали ингредиента"]')
CLOSE_BUTTON = (By.XPATH, ".//button[contains(@class,'close')]")
INGREDIENT_COUNTER = (By.XPATH, "(.//p[contains(@class, 'counter_counter__num__3nue1')])[1]")
ORDER = (By.XPATH, "//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (верх)']")