from tests.pages.sign_in_page import SignInPage
from tests.testcases.test_base import TestBase
import allure

from tests.utilities import messages, constants


class TestCase001(TestBase):
    sign_in_page = SignInPage()

    @allure.title("Test incorrect account")
    def test_case_id_001(self):
        self.sign_in_page.type_email("incorrect_account_blah")
        self.sign_in_page.click_email_next_button()
        # assert self.sign_in_page.get_sign_in_error() == messages.WRONG_ACCOUNT_ERROR
        assert self.sign_in_page.get_sign_in_error() == "Không thể tìm thấy Tài khoản Google của bạn"
