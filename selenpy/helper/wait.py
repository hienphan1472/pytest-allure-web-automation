import time
from selenium.common.exceptions import StaleElementReferenceException


def wait_until(condition, error=None, timeout=5, polling=0.5):
    max_time = time.time() + timeout
    not_found = None
    while time.time() < max_time:
        try:
            if condition():
                return
        except StaleElementReferenceException as err:
            not_found = err
        else:
            not_found = None
        time.sleep(polling)
    raise RuntimeError(not_found or error)
