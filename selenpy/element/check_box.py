from selenpy.element.base_element import BaseElement


class CheckBox(BaseElement):

    def __init__(self, locator):
        super().__init__(locator)

    def is_checked(self):
        return self.find_element().is_selected()

    def check(self):
        if not self.is_checked():
            self.click()

    def un_check(self):
        if self.is_checked():
            self.click()
