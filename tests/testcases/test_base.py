import pytest

from selenpy.support import browser
import logging


class TestBase:

    @pytest.fixture(scope="class", autouse=True)
    def setup(self, request):
        logging.info("Starting the test on " + str(pytest.browser_name))
        browser.start_driver(pytest.browser_name, pytest.remote_host)
        browser.maximize_browser()
        browser.open_url(pytest.url)

        request.cls.driver = browser.get_driver()
        # Close all browsers when tests have been finished
        yield
        browser.quit_all()
