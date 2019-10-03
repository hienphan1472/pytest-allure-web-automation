from selenpy.element.base_element import BaseElement


class TextBox(BaseElement):

    def __init__(self, locator):
        super().__init__(locator)

    @property
    def value(self):
        return self.get_attribute("value")

    def enter(self, text):
        element = self.find_element()
        element.clear()
        element.send_keys(text)
