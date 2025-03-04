from pages.base_page import BasePage
from locators.main_page import *
import urls

class MainPage(BasePage):
    def open(self):
        self._open_page(urls.MAIN_PAGE)

    def click_personal_account_href(self):
        self._click_locator(PERSONAL_ACCOUNT_HREF)