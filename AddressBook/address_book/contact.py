from .utils import valid_name, valid_email, valid_tel_number, valid_birthday,\
     convert_date_format


class NameDescriptor:
    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        value = valid_name(value)
        if not value:
            raise ValueError("This field can't be empty and can include only letters at least two and '-'.")
        setattr(instance, self.name, value)


class MiddleNameDescriptor:
    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if value:
            value = valid_name(value)
            if not value:
                raise ValueError("This field can be empty and can include only letters at least two and '-'.")
        setattr(instance, self.name, value)


class TelNumberDescriptor:
    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        value = valid_tel_number(value)
        if not value:
            raise ValueError("Invalid telephone number.")
        setattr(instance, self.name, value)


class EmailDescriptor:
    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not valid_email(value):
            raise ValueError("Invalid email address.")
        setattr(instance, self.name, value)


class BirthdayDescriptor:
    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not valid_birthday(value):
            raise ValueError("Invalid birthday format.")
        value = convert_date_format(value)
        setattr(instance, self.name, value)


class Contact:
    """
    A class representing a contact in an address book.
    """
    first_name = NameDescriptor()
    middle_name = MiddleNameDescriptor()
    last_name = NameDescriptor()
    tel_number = TelNumberDescriptor()
    email = EmailDescriptor()
    birthday = BirthdayDescriptor()

    def __init__(self, first_name: str = "", middle_name: str = "", last_name: str = "", birthday: str = "",
                 tel_number: str = "", email: str = "") -> None:
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.birthday = birthday
        self.tel_number = tel_number
        self.email = email

