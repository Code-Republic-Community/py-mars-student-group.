import unittest
import sys
sys.path.append('/Users/jon/Workspace/py-mars-student-group/AddressBook')
from address_book.address_book import Contact
from datetime import datetime
from re import match


class TestContact(unittest.TestCase):
    def test_properties(self):
        contact = Contact()

        # Test setting properties
        contact.first_name = "Robert"
        contact.middle_name = "De"
        contact.last_name = "Niro"
        contact.birthday = "01.01.80"
        contact.tel_number = "37491111111"
        contact.email = "rdn0101@gmail.com.com"

        self.assertEqual(contact.first_name, "Robert")
        self.assertEqual(contact.middle_name, "De")
        self.assertEqual(contact.last_name, "Niro")
        self.assertEqual(contact.birthday, "01.01.80")
        self.assertEqual(contact.tel_number, "37491111111")
        self.assertEqual(contact.email, "rdn0101@gmail.com.com")

    def test_valid_first_last_names(self):
        # Test first_name, last_name attributes
        contact = Contact()
        contact.first_name = self.valid_name("Robert")
        contact.last_name = self.valid_name("Niro")
        self.assertEqual(contact.first_name, True)
        self.assertEqual(contact.last_name, True)

    def test_name_attribute(self):
        # Test name attribute when all name parts are provided
        contact_with_middle_name = Contact(first_name="Robert", middle_name="De", last_name="Niro")
        self.assertEqual(contact_with_middle_name.name, "Robert De Niro")

        # Test name attribute when middle name is missing
        contact_without_middle_name = Contact(first_name="Tom", last_name="Smith")
        self.assertEqual(contact_without_middle_name.name, "Tom Smith")

    def test_birthday_format(self):
        # Test without converting the birthday format
        contact = Contact(birthday="01.01.80")
        self.assertEqual(contact.birthday, "01.01.80")

        # Test converting the birthday format
        contact.birthday = self.convert_date_format("02.03.85")
        self.assertEqual(contact.birthday, "02.Mar.1985")

    def test_valid_tel_number(self):
        contact = Contact()
        contact.tel_number = self.valid_tel_number("098765432")
        self.assertEqual(contact.tel_number, True)
        contact.tel_number = self.valid_tel_number("37498765432")
        self.assertEqual(contact.tel_number, True)

    def test_valid_email(self):
        contact = Contact()
        contact.email = self.valid_email("john@example.com")
        self.assertEqual(contact.email, True)

    @staticmethod
    def valid_tel_number(tel_number: str) -> bool:
        valid_oper = ["93", "94", "98", "91", "43", "11"]
        if tel_number.isdigit() and (
                tel_number[0] == "0" and tel_number[1:3] in valid_oper and len(tel_number[3:]) == 6) or \
                (tel_number[0:3] == "374" and tel_number[3:5] in valid_oper and len(tel_number[5:]) == 6):
            return True
        return False

    @staticmethod
    def valid_email(email: str) -> bool:
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return match(pattern, email) is not None

    @staticmethod
    def valid_name(name: str) -> bool:
        min_length = 2
        max_length = 50
        allowed_characters = r"^[A-Za-z -]+$"
        if len(name) < min_length or len(name) > max_length:
            return False
        if not match(allowed_characters, name):
            return False
        return True

    @staticmethod
    def convert_date_format(input_date: str) -> str:
        date = datetime.strptime(input_date, "%d.%m.%y")
        if date.year > datetime.now().year:
            date = date.replace(year=date.year - 100)
        result = date.strftime("%d.%b.%Y")
        return result


if __name__ == '__main__':
    unittest.main()