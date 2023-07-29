import json
from .contact import Contact


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

            The address book is saved as a JSON formatted stream to the file specified by the path "data/address_book_data.json".
            Each contact in the address book is represented as a dictionary with the contact's telephone number as the key
            and a list of contact details (first name, middle name, last name, birthday, and email) as the value.
        """
        with open(r"data\address_book_data.json", "w") as f:
            for contact in my_address_book.contacts:
                json.dump({contact.tel_number: [contact.first_name, contact.middle_name, contact.last_name, contact.birthday, contact.email]}, f)
                f.write("\n")

    def load_address_book(self, my_address_book):
        """
            Loads the address book from a JSON file.

            Parameters:
                my_address_book (AddressBook): The AddressBook object where the loaded contacts will be stored.

            The address book is loaded from the JSON file specified by the path "data/address_book_data.json".
            Each line in the JSON file represents a contact in the address book, serialized as a JSON object.
            The contact details are extracted from each JSON object and a new Contact object is created and added to the address book.
        """
        with open(r"data\address_book_data.json", "r") as f:
            for line in f:
                data = json.loads(line)
                for k, v in data.items():
                    contact = Contact(v[0], v[1], v[2], v[3], k, v[4])
                    my_address_book.contacts.append(contact)


