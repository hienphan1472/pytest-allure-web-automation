from selenium import webdriver
from selenpy.browser.driver import Driver
from webdriver_manager.chrome import ChromeDriverManager


class ChromeDriver(Driver):

    def create_driver(self, remote_host):
        options = webdriver.ChromeOptions()
        if remote_host is None:
            self._driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                            options=options)
        else:
            self._driver = webdriver.Remote(command_executor=remote_host)
        return self
