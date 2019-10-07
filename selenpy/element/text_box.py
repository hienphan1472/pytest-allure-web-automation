import logging

from selenpy.element.base_element import BaseElement


class TextBox(BaseElement):

    def __init__(self, locator):
        self.__locator = locator
        super().__init__(locator)

    @property
    def value(self):
        return self.get_attribute("value")

    def enter(self, text):
        logging.info(f"type text '{text}' to element by locator: {self.__locator}")
        element = self.find_element()
        element.clear()
        element.send_keys(text)
