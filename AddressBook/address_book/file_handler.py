import json
from .contact import Contact
import os

class FileHandler:
    """
    The FileHandler class is responsible for saving and loading an address book to/from a JSON file.

        Methods:
            save_address_book(my_address_book): Saves the address book to a JSON file.
            load_address_book(my_address_book): Loads the address book from a JSON file.
    """

    def save_address_book(self, my_address_book):
        """
        Saves the address book to a JSON file.

        Parameters:
            my_address_book (AddressBook): The AddressBook object representing the address book to be saved.

        Description:
            This method takes an AddressBook object and serializes its contacts to a JSON formatted file. The contacts
            are represented as lists of contact details, including first name, middle name, last name, birthday, telephone
            number, and email. The serialized data is written to the file specified by the path "data/address_book_data.json".
        """
        with open(r"data/address_book_data.json", "w") as f:
            json.dump([
                [contact.first_name,
                 contact.middle_name,
                 contact.last_name,
                 contact.birthday,
                 contact.tel_number,
                 contact.email]
                for contact in my_address_book.contacts], f, indent=2)

    def load_address_book(self, my_address_book):
        """
        Loads the address book from a JSON file.

        Parameters:
            my_address_book (AddressBook): The AddressBook object where the loaded contacts will be stored.

        Description:
            This method reads data from a JSON file specified by the path "data/address_book_data.json".
            Each contact in the file is represented as a list of contact details, including first name, middle name,
            last name, birthday, telephone number, and email. The method deserializes the data and creates Contact objects
            using the contact details. These Contact objects are then added to the provided AddressBook object.
        """
        with open(r"data/address_book_data.json", "r") as f:
            if f.read(0) != '':
                f.seek(0)  # it may be redundant but it does not hurt
                data = json.load(f)
            
                for contact_info in data:
                    my_address_book.contacts.append(Contact(*contact_info))



