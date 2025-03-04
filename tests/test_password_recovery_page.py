from faker import Faker
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage

import urls

from time import sleep


class TestPasswordRecoveryPage:
    def test_open_password_recovery_page_by_click_password_recovery_href(self, page_driver):
        login_page = LoginPage(page_driver)
        login_page.open()
        login_page.click_password_recovery_href()
        current_url = page_driver.current_url
        assert current_url == urls.FORGOT_PASSWORD_PAGE

    def test_enter_email_and_click_recovery_button_success(self, page_driver):
        forgot_password_page = ForgotPasswordPage(page_driver)
        forgot_password_page.open()
        fake = Faker()
        forgot_password_page.set_email(fake.email())
        forgot_password_page.click_recovery_button()
        current_url = page_driver.current_url
        assert current_url == urls.RESET_PASSWORD_PAGE

    def test_make_password_field_active(self, page_driver):
        forgot_password_page = ForgotPasswordPage(page_driver)
        forgot_password_page.open()
        forgot_password_page.click_recovery_button()
        reset_password_page = ResetPasswordPage(page_driver)
        reset_password_page.click_on_show_password_button()
        assert reset_password_page.is_field_password_active()