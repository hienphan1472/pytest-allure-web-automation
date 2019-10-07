import logging

from selenpy.element.base_element import BaseElement


class IFrame(BaseElement):

    def __init__(self, locator):
        self.__locator = locator
        super().__init__(locator)

    def select(self):
        logging.info(f"select frame by locator: {self.__locator}")
        self._driver.switch_to.frame(self.find_element())

    def deselect(self):
        logging.info(f"deselect frame by locator: {self.__locator}")
        self._driver.switch_to.default_content()
