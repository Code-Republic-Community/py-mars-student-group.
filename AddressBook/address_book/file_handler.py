import json
from .contact import Contact
import os


class FileHandler:
    """
        The FileHandler class provides methods to save and load address book data in JSON format.
        Methods:
            save_address_book(self, my_address_book): Save address book data to a JSON file.
            load_address_book(self, my_address_book): Load address book data from a JSON file.
        """

    def save_address_book(self, my_address_book, data_file_path):
        """
            Save address book data to a JSON file.
        """
        def strip_leading_underscore(contact_dict):
            return {key.strip('_'): value for key, value in contact_dict.items()}
        with open(data_file_path, "w") as f:
            json.dump([strip_leading_underscore(vars(contact)) for contact in my_address_book.contacts.values()], f,
                      indent=2)

    def load_address_book(self, my_address_book, data_file_path):
        """
            Load address book data from a JSON file.
        """
        with open(data_file_path, "r") as f:
            data = json.load(f)
            for contact_info in data:
                my_address_book.contacts[contact_info["tel_number"]] = Contact(**contact_info)
