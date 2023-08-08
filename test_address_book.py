# import failed in the tests folder, so I created it in this folder

import unittest

from AddressBook.address_book import Address_Book



class TestAddressBook(unittest.TestCase):
    def setUp(self):
        self.address_book = Address_Book()
        
        
    
    def test_add_contact(self):
        self.address_book.add_contact("name","077777777","name@domen.com","11-11-2011")
        
        self.assertEqual(len(self.address_book.contacts),1)
        contact = list(self.address_book.contacts.values())[0]
        
        self.assertEqual(contact.name,"name")
        self.assertEqual(contact.phone_number,"077777777")
        self.assertEqual(contact.email_address,"name@domen.com")
        self.assertEqual(contact.birthday,"11-11-2011")
        
    
        
    
    def test_dell_contact(self):
        self.address_book.add_contact("name","077777777","name@domen.com","11-11-2011")
        contact = list(self.address_book.contacts.values())[0]
        
        self.address_book.dell_contact(contact)
    
        self.assertEqual(len(self.address_book.contacts),0)
        
        
        
if __name__ == '__main__':
    unittest.main()
    