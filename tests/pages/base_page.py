import logging
import time
import allure

from selenpy.element.base_element import BaseElement
from selenpy.support import browser
import pytest


class BasePage:
    def __init__(self):
        self.ele_common_element = BaseElement("//common/xpath/")

    def open(self, url):
        browser.open_url(url)

    def open_from_base(self, url, base=pytest.url):
        logging.info(base + url)
        self.open(base + url)

    def open_home_page(self):
        """
        Open home page
        """
        self.open(pytest.url)

    @allure.step("logout")
    def logout(self):
        """
        Logout current account
        :return:
        """
        browser.execute_script("javascript:logout();")

    def wait(self, seconds):
        time.sleep(seconds)

    def refresh(self):
        browser.get_driver().refresh()
