import re
import validators


def is_valid_name(name: str):
    return len(name) > 1 and name.isalpha()


def is_valid_telephone(tel: str):
    return (len(tel) == 12 and tel.startswith('+374') and tel[4:].isdigit()) or \
        (len(tel) == 9 and tel.startswith('0') and tel.isdigit())


def is_valid_address(address: str):
    pattern = r"^[a-zA-Z0-9\s/]+$"
    return re.match(pattern, address)


def is_valid_url(url: str):
    return validators.url(url)


def is_valid_mail(mail: str):
    pattern = r"[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z]+"
    return re.match(pattern, mail)

