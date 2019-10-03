from selenpy.support.driver_manager import DriverManager
from ..common.config import timeout

__driver = {}


def start_driver(name, remote_host, driver_key="default"):
    driver = DriverManager().start_driver(name, remote_host)
    driver.get_driver().implicitly_wait(timeout)
    __driver[driver_key] = driver
    Key.current = driver_key


def get_driver():
    return __driver[Key.current].get_driver()


def switch_to_driver(driver_key="default"):
    Key.current = driver_key


def close_browser():
    get_driver().close()


def quit_all():
    [__driver[key].get_driver().quit() for key in __driver]
    __driver.clear()


class Key:
    current = "default"
