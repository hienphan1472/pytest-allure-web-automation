import logging
import time

from selenium.common.exceptions import StaleElementReferenceException

from selenpy.element.base_element import BaseElement
from selenium.webdriver.support.ui import Select


class ComboBox(BaseElement):

    def __init__(self, locator):
        super().__init__(locator)

    def select_by_value(self, value):
        Select(self.find_element()).select_by_value(value)

    def select_by_index(self, idx):
        Select(self.find_element()).select_by_index(idx)

    def select_by_visible_text(self, text):
        try:
            Select(self.find_element()).select_by_visible_text(text)
        except StaleElementReferenceException as e:
            logging.warning(e)
            time.sleep(1)
            Select(self.find_element()).select_by_visible_text(text)

    @property
    def first_selected_text(self):
        try:
            return Select(self.find_element()).first_selected_option.text
        except StaleElementReferenceException as e:
            logging.warning(e)
            time.sleep(1)
            return Select(self.find_element()).first_selected_option.text

    @property
    def option_size(self):
        return len(Select(self.find_element()).options)
