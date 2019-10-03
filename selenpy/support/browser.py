from selenpy.support import factory


def get_driver():
    return factory.get_driver()


def get_title():
    return get_driver().title


def maximize_browser():
    get_driver().maximize_window()


def open_url(url):
    get_driver().get(url)


def switch_to_driver(driver_key="default"):
    factory.switch_to_driver(driver_key)


def close_browser():
    factory.close_browser()


def quit_all():
    factory.quit_all()


def start_driver(name, remote_host, key="default"):
    factory.start_driver(name, remote_host, key)


def execute_script(scripts):
    return get_driver().execute_script(scripts)


def switch_to_new_window():
    new_window = get_driver().window_handles[1]
    get_driver().switch_to.window(new_window)


def get_current_url():
    return get_driver().current_url
