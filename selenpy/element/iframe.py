from selenpy.element.base_element import BaseElement


class IFrame(BaseElement):

    def __init__(self, locator):
        super().__init__(locator)

    def select(self):
        self._driver.switch_to.frame(self.find_element())

    def deselect(self):
        self._driver.switch_to.default_content()
