from pages.base_page import BasePage
from locators.account_profile_page import *

class AccountProfilePage(BasePage):
    def click_order_history_button(self):
        self._click_locator(ORDERS_HISTORY_BUTTON)