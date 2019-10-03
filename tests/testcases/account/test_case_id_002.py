from tests.pages.sign_in_page import SignInPage
from tests.testcases.test_base import TestBase
import allure

from tests.utilities import messages, constants


class TestCase002(TestBase):
    sign_in_page = SignInPage()

    @allure.title("Test incorrect password")
    def test_case_id_002(self):
        self.sign_in_page.type_email(constants.USER_EMAIL)
        self.sign_in_page.click_email_next_button()
        self.sign_in_page.type_password("invalid password")
        self.sign_in_page.click_password_next_button()
        assert self.sign_in_page.get_sign_in_error() == messages.WRONG_PASSWORD_ERROR
