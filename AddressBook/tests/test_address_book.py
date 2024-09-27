import unittest
import sys

from ..address_book.contact import Contact
from ..address_book.address_book import AddressBook
from unittest.mock import patch
import io


class TestAddressBook(unittest.TestCase):
    def setUp(self):
        self.address_book = AddressBook()

    def test_add_contact(self):
        # Simulate user input for adding a contact
        with patch("builtins.input", side_effect=["Tom", "", "Smith", "01.12.20", "093420841", "Tom.Smith@gmail.com"]):
            with patch("sys.stdout", new=io.StringIO()) as fake_output:
                self.address_book.add_contact()

        # Check if the contact was added to the contacts list
        self.assertEqual(len(self.address_book.contacts), 1)
        contact = list(self.address_book.contacts.values())[0]
        self.assertEqual(contact.first_name, "Tom")
        self.assertEqual(contact.last_name, "Smith")
        self.assertEqual(contact.middle_name, "")
        self.assertEqual(contact.birthday, "01.Dec.2020")
        self.assertEqual(contact.tel_number, "093420841")
        self.assertEqual(contact.email, "Tom.Smith@gmail.com")

        # Check if the success message is printed
        expected_output = "Contact was added successfully!"
        self.assertIn(expected_output, fake_output.getvalue())

    def test_delete_contact(self):
        # Add a contact for testing
        contact = Contact("Jane", "", "Smith", "01.12.20", "093420841", "john.doe@example.com")
        self.address_book.contacts[contact.tel_number] = contact

        # Simulate user input for deleting a contact by telephone number
        with patch("builtins.input", side_effect=["1", "093420841", "yes"]):
            with patch("sys.stdout", new=io.StringIO()) as fake_output:
                self.address_book.delete_contact()

        # Check if the contact was deleted from the contacts list
        self.assertEqual(len(self.address_book.contacts), 0)
        expected_output = "Contact was deleted successfully!"

        with patch("builtins.input", side_effect=["1", "093420841", "no"]):
            with patch("sys.stdout", new=io.StringIO()) as fake_output:
                self.address_book.delete_contact()

        # Check if the cancellation message is printed
        expected_output = "The contact is not deleted."










if __name__ == '__main__':
    unittest.main()
