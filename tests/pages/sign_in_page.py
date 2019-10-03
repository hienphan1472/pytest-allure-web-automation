import logging

from selenpy.element.base_element import BaseElement
from selenpy.element.text_box import TextBox
from selenpy.element.button import Button
from tests.utilities import constants
from .base_page import BasePage


class SignInPage(BasePage):

    def __init__(self):
        super().__init__()
        self.txt_user_name = TextBox("id=identifierId")
        self.btn_email_next = Button("id=identifierNext")
        self.txt_password = TextBox("css=input[type='password']")
        self.btn_password_next = Button("id=passwordNext")
        self.ele_error = BaseElement("css=form[method='post'] div[aria-live='assertive'] div")

    def type_email(self, email):
        self.txt_user_name.enter(email)

    def click_email_next_button(self):
        self.btn_email_next.click()

    def type_password(self, password):
        self.txt_password.wait_for_visible(constants.MEDIUM_TIMEOUT)
        self.txt_password.enter(password)

    def click_password_next_button(self):
        self.btn_password_next.click()

    def get_sign_in_error(self):
        return self.ele_error.text

    def sign_in(self, email, password):
        self.txt_user_name.wait_for_invisible(constants.MEDIUM_TIMEOUT)
        self.type_email(email)
        self.click_email_next_button()
        self.type_password(password)
        self.click_password_next_button()
