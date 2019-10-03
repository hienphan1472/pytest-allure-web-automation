from faker import Faker
from faker.providers import internet, credit_card
import logging
from tests.utilities import constants, utils

__cards = {
    1: "5555555555554444",
    2: "5200828282828210"
}


def get_email(domain=None):
    faker = Faker()
    faker.add_provider(internet)
    email = faker.email(domain)
    logging.info("Generated email: " + email)
    return email


def get_default_password():
    return "Ifonly@1234"


def get_card_number():
    faker = Faker()
    faker.add_provider(credit_card)
    return faker.credit_card_number("mastercard")


def get_first_name():
    faker = Faker()
    return faker.first_name()


def get_last_name():
    faker = Faker()
    return faker.last_name()


def get_user_info(card_randomly=True, index=1):
    first = get_first_name()
    last = get_last_name()
    number = get_card_number()
    if not card_randomly:
        number = __cards[index]
    return first, last, first + " " + last, number, number[0:6] + "********"


def get_password():
    faker = Faker()
    password = faker.password()
    logging.info("Generated password: " + password)
    return password


def get_gmail():
    gmail = '%s+%s@gmail.com' % (constants.GMAIL_USER_NAME, str(utils.current_milli_time()))
    logging.info("Generated email: " + gmail)
    return gmail
