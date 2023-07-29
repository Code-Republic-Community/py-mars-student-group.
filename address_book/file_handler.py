import json

from address_book.address_book import AddressBook
from address_book.contact import Contact

def save_address_book(filename, address_book):
    with open(filename, 'w') as file:
        json.dump([vars(contact) for contact in address_book.contacts], file, indent=4)

def load_address_book(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        address_book = AddressBook()
        for contact_data in data:
            address_book.add_contact(Contact(**contact_data))
        return address_book