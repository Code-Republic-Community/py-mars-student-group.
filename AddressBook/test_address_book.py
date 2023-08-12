import unittest
from address_book import address_book.Addressbook
from address_book import Contact


class TestAddressbook(unittest.TestCase):
    def test_add_contact(self):
        addressbook = Addressbook()
        contact = Contact("Anna", "Doe", "ann@example.com", "Abovyan 45/12", "+37445678944",
                          "https://translate.google.com/")
        addressbook.add_contact(contact)
        self.assertEqual(len(addressbook.contacts), 1)

    def test_search_contact(self):
        addressbook = Addressbook()
        contact = Contact("Anna", "Doe", "ann@example.com", "Abovyan 45/12", "+37445678944",
                          "https://translate.google.com/")
        addressbook.add_contact(contact)
        result = addressbook.search_contact("Anna")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], contact.dict_form)

    def test_update_contact(self):
        addressbook = Addressbook()  # Create an empty address book
        contact = Contact("Anna", "Doe", "ann@example.com", "Abovyan 45/12", "+37445678944",
                          "https://translate.google.com/")
        addressbook.add_contact(contact)
        upd_contact = Contact("Anna", "Davtyan", "ann@example.com", "Abovyan 45/12", "+37445678944",
                          "https://translate.google.com/")
        addressbook.update_contact("John", upd_contact)

        updated_contact_data = addressbook.get_contact("Anna")
        self.assertEqual(updated_contact_data, upd_contact.dict_form)

    def test_delete_contact(self):
        addressbook = Addressbook()  # Create an empty address book
        contact = Contact("Anna", "Doe", "ann@example.com", "Abovyan 45/12", "+37445678944",
                          "https://translate.google.com/")
        addressbook.add_contact(contact)
        addressbook.delete_contact("Anna")
        self.assertEqual(len(addressbook.contacts), 0)

    if __name__ == '__main__':
        unittest.main()