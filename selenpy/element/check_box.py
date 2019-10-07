import logging

from selenpy.element.base_element import BaseElement


class CheckBox(BaseElement):

    def __init__(self, locator):
        self.__locator = locator
        super().__init__(locator)

    def is_checked(self):
        logging.info(f"is checkbox checked by locator: {self.__locator}")
        return self.find_element().is_selected()

    def check(self):
        logging.info(f"check the checkbox by locator: {self.__locator}")
        if not self.is_checked():
            self.click()

    def un_check(self):
        logging.info(f"uncheck the checkbox by locator: {self.__locator}")
        if self.is_checked():
            self.click()
