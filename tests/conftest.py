import allure
import moment
import pytest


def pytest_addoption(parser):
    parser.addoption("--remote-host", action="store", help="Remote server for execution. http://127.0.0.1:4444/wd/hub",
                     metavar="")
    parser.addoption("--driver", action="store", help="Browsers under test. It should be: chrome, firefox",
                     metavar="")
    parser.addoption("--url", action="store", help="The url of AUT", metavar="")


def pytest_configure(config):
    pytest.remote_host = config.getoption("--remote-host", None)
    pytest.browser_name = config.getoption("--driver", "chrome", True)
    pytest.url = config.getoption("--url", "https://mail.google.com/mail/", True)


def pytest_exception_interact(node, report):
    if node and report.failed:
        driver = node.funcargs.get('request').cls.driver
        if driver is not None:
            class_name = node._nodeid.split(".py::")[-1].replace("::", "_class_")
            save_screenshot(driver, class_name)


def remove_special_characters(text):
    return text.translate({ord(i): None for i in '\ / : * ? " < > |'})


def save_screenshot(driver, name):
    now = moment.now().strftime("%d-%m-%Y")
    _name = remove_special_characters(name)
    allure.attach(driver.get_screenshot_as_png(), _name + "_" + now, attachment_type=allure.attachment_type.PNG)
