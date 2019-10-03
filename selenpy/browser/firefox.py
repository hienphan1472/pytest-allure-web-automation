from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenpy.browser.driver import Driver


class FirefoxDriver(Driver):

    def create_driver(self, remote_host):
        options = webdriver.FirefoxOptions()
        if remote_host is None:
            self._driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                             options=options)
        else:
            self._driver = webdriver.Remote(command_executor=remote_host)
        return self
