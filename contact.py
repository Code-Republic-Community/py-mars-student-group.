import time
import json
import re

class ContactDescriptor:
    """Descriptor for managing contact attributes."""
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance , owner):
        if instance is None:
            return self
        if self.name not in instance.__dict__:
            raise AttributeError(f"'{owner.__name__}' object has no attribute '{self.name}'")
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value



class Contact:
    """Class representing a contact."""


    name = ContactDescriptor()
    phone_number = ContactDescriptor()
    email = ContactDescriptor()
    birthday = ContactDescriptor()

    def __init__(self, name, phone_number, email, birthday ):
        """Initialize the contact with name, phone_number, email, and birthday."""
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.birthday = birthday
        self.contact_dict = {
            'name': name,
            'phone_number': phone_number,
            'email': email,
            'birthday': birthday
        }
