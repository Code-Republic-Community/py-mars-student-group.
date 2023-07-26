import json
from .contact import Contact


class FileHandler:

    def save_address_book(self, my_address_book):
        with open(r"data\address_book_data.json", "w") as f:
            for contact in my_address_book.contacts:
                json.dump({contact.tel_number: [contact.first_name, contact.middle_name, contact.last_name, contact.birthday, contact.email]}, f)

    def load_address_book(self, my_address_book):
        with open(r"data\address_book_data.json", "r") as f:
            for line in f:
                data = json.loads(line)
                for k, v in data.items():
                    contact = Contact(v[0], v[1], v[2], v[3], k, v[4])
                    my_address_book.contacts.append(contact)


