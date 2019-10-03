import re
import time
import allure
import requests
from datetime import datetime


def get_urls(text):
    text = text.replace('=\n', '').replace('\r', '')
    return re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)


def current_milli_time():
    return int(round(time.time() * 1000))


@allure.step("Check file exist on server")
def is_remote_file_existed(url):
    return requests.get(url).status_code == 200


def format_preferred_date(date_time_str):
    date_time_obj = datetime.strptime(date_time_str, '%m/%d/%Y %H:%M %p')
    return "%s %s" % (date_time_obj.date().strftime("%m/%d/%y"), date_time_obj.time().strftime("%-H:%M %p"))


def extract_number(text):
    return re.findall(r'\d+', text)
