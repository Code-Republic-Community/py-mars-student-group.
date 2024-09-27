import unittest
from AddressBook.address_book.contact import Contact


class TestContactClass(unittest.TestCase):
    def test_contact_class_attributes(self):
        contact = Contact(first_name="John", middle_name="",  last_name="Doe", birthday="01.12.88",
                          tel_number="098801212", email="john.doe@example.com")
        self.assertEqual(contact.first_name, "John")
        self.assertEqual(contact.middle_name, "")
        self.assertEqual(contact.last_name, "Doe")
        self.assertEqual(contact.birthday, "01.Dec.1988")
        self.assertEqual(contact.tel_number, "098801212")
        self.assertEqual(contact.email, "john.doe@example.com")

    def test_contact_class_invalid_attributes(self):
        # Test invalid first name
        with self.assertRaises(ValueError):
            Contact(first_name="J")

        # Test invalid email
        with self.assertRaises(ValueError):
            Contact(email="invalid_email")

        # Test invalid telephone number
        with self.assertRaises(ValueError):
            Contact(tel_number="123-456-7890")


if __name__ == '__main__':
    unittest.main()

