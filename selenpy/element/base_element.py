import logging
import time

from selenpy.support import browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException, \
    StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenpy.common import config
from selenium.webdriver.common.action_chains import ActionChains
from selenpy.helper.wait import wait_until


class BaseElement:

    def __init__(self, locator):
        self.__strategies = {
            'id': self._find_by_id,
            'name': self._find_by_name,
            'xpath': self._find_by_xpath,
            'css': self._find_by_css_selector,
            'class': self._find_by_class_name
        }
        self.__locator = locator
        self.__dynamic_locator = locator

    @property
    def _driver(self):
        return browser.get_driver()

    @property
    def _element(self):
        return self.find_element()

    @property
    def text(self):
        logging.info(f"get element text by locator: {self.__locator}")
        return self.find_element().text

    def format(self, *args):
        self.__locator = self.__dynamic_locator % args

    def find_element(self):
        prefix, criteria = self.__parse_locator(self.__locator)
        strategy = self.__strategies[prefix]
        return strategy(criteria)

    def click(self):
        try:
            logging.info(f"click on element by locator: {self.__locator}")
            wait_until(lambda: self.is_enabled())
            self._element.click()
        except ElementClickInterceptedException as e:
            sources = self._driver.page_source
            file = open('page-source.txt', 'w', encoding='utf-8')
            file.write(sources)
            file.close()
            raise e

    def delay(self, seconds):
        time.sleep(seconds)

    def get_attribute(self, name):
        logging.info(f"get element attribute '{name}' by locator: {self.__locator}")
        return self._element.get_attribute(name)

    def send_keys(self, *value):
        logging.info(f"send keys '{value}' to element by locator: {self.__locator}")
        self._element.send_keys(value)

    def __parse_locator(self, locator):
        if locator.startswith(('//', '(//')):
            return 'xpath', locator
        index = self.__get_locator_separator_index(locator)
        if index != -1:
            prefix = locator[:index].strip()
            if prefix in self.__strategies:
                return prefix, locator[index + 1:].lstrip()
        return 'default', locator

    def __by(self, prefix):
        if prefix == "class":
            return By.CLASS_NAME
        elif prefix == "css":
            return By.CSS_SELECTOR
        else:
            return prefix

    def __get_locator_separator_index(self, locator):
        if '=' not in locator:
            return locator.find(':')
        if ':' not in locator:
            return locator.find('=')
        return min(locator.find('='), locator.find(':'))

    def _find_by_id(self, criteria):
        return WebDriverWait(self._driver, config.timeout).until(EC.presence_of_element_located((By.ID, criteria)))

    def _find_by_name(self, criteria):
        return WebDriverWait(self._driver, config.timeout).until(EC.presence_of_element_located((By.NAME, criteria)))

    def _find_by_xpath(self, criteria):
        return WebDriverWait(self._driver, config.timeout).until(EC.presence_of_element_located((By.XPATH, criteria)))

    def _find_by_css_selector(self, criteria):
        return WebDriverWait(self._driver, config.timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, criteria)))

    def _find_by_class_name(self, criteria):
        return WebDriverWait(self._driver, config.timeout).until(
            EC.presence_of_element_located((By.CLASS_NAME, criteria)))

    def is_displayed(self, timeout=None):
        try:
            logging.info(f"is element displayed by locator: {self.__locator}")
            return self.wait_for_visible(timeout).is_displayed()
        except (NoSuchElementException, TimeoutException, StaleElementReferenceException):
            return False
        except Exception as e:
            raise e

    def move_to(self):
        logging.info(f"move to element by locator: {self.__locator}")
        actions = ActionChains(self._driver)
        actions.move_to_element(self._element).perform()

    def is_enabled(self):
        logging.info(f"is element enabled by locator: {self.__locator}")
        return self._element.is_enabled()

    def is_selected(self):
        logging.info(f"is element selected by locator: {self.__locator}")
        return self._element.is_selected()

    def wait_for_visible(self, timeout=None):
        if timeout is None:
            timeout = config.timeout
        prefix, criteria = self.__parse_locator(self.__locator)
        logging.info(f"wait for element visible by locator: {self.__locator}")
        return WebDriverWait(self._driver, timeout).until(
            EC.visibility_of_element_located((self.__by(prefix), criteria)))

    def wait_for_invisible(self, timeout=None):
        if timeout is None:
            timeout = config.timeout
        prefix, criteria = self.__parse_locator(self.__locator)
        logging.info(f"wait for element invisible by locator: {self.__locator}")
        WebDriverWait(self._driver, timeout).until(EC.invisibility_of_element_located((self.__by(prefix), criteria)))

    def wait_for_presence(self, timeout=None):
        if timeout is None:
            timeout = config.timeout
        prefix, criteria = self.__parse_locator(self.__locator)
        logging.info(f"wait for element presence by locator: {self.__locator}")
        return WebDriverWait(self._driver, timeout).until(
            EC.presence_of_element_located((self.__by(prefix), criteria)))

    def scroll_into_view(self):
        logging.info(f"scroll element into view by locator: {self.__locator}")
        self._driver.execute_script("arguments[0].scrollIntoView();", self._element)
