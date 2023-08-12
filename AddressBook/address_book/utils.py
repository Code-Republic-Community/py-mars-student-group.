from datetime import datetime
from re import match
from typing import Union


def valid_tel_number(tel_number: str) -> Union[str, bool]:
    """
    Validates the telephone number format for Armenian numbers.
    """
    valid_oper = ["93", "94", "98", "91", "43", "11"]
    tel_number = tel_number.strip().replace(" ", "").replace("-", "")
    if tel_number.isdigit() and (tel_number[0] == "0" and tel_number[1:3] in valid_oper and len(tel_number[3:]) == 6) \
            or (tel_number[0:3] == "374" and tel_number[3:5] in valid_oper and len(tel_number[5:]) == 6):
        if len(tel_number) == 11 and tel_number[0:3] == "374":
            tel_number = tel_number[0:3].replace("374", "0") + tel_number[3:]
        return tel_number
    return False


def valid_email(email: str) -> Union[str, bool]:
    """
    Validates the email address using a regular expression pattern.
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if match(pattern, email) is not None:
        return email.strip()
    return False


def valid_name(name: str) -> Union[str, bool]:
    """
    Validates the name to include only letters, spaces, and hyphens with a minimum length of 2 characters.
    """
    min_length = 2
    max_length = 50
    allowed_characters = r"^[A-Za-z -]+$"
    if len(name) < min_length or len(name) > max_length or not match(allowed_characters, name):
        return False
    return name.strip().title()


def valid_birthday(input_date: str) -> Union[str, bool]:
    """
        Validate a given input date string representing a birthday.
    """
    try:
        datetime.strptime(input_date, "%d.%b.%Y")
        return input_date
    except ValueError:
        try:
            datetime.strptime(input_date, "%d.%m.%y")
            return input_date
        except ValueError:
            return False


def convert_date_format(input_date: str) -> str:
    """
    Converts the date format from DD.MM.YY to DD.b.YYYY (e.g., 01.12.20 to 01.Dec.2020).
    """
    try:
        date = datetime.strptime(input_date, "%d.%m.%y")
    except ValueError:
        try:
            date = datetime.strptime(input_date, "%d.%b.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Supported formats are 'DD.MM.YY' and 'DD.b.YYYY'.")

    if date.year > datetime.now().year:
        date = date.replace(year=date.year - 100)
    result = date.strftime("%d.%b.%Y")
    return result





