from pages.base_page import BasePage
import urls

class MainPage(BasePage):
    def open(self):
        self.open_page(urls.MAIN_PAGE)