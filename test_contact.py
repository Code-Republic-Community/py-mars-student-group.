# import failed in the tests folder, so I created it in this folder


import unittest
from AddressBook.contact import Contact




class TestContact(unittest.TestCase):

        
    def test_contact_class_attributes(self):
        contact = Contact("name","077777777","name@domen.com","11-11-2011")
        
        self.assertEqual(contact.name,"name")
        self.assertEqual(contact.phone_number,"077777777")
        self.assertEqual(contact.email_address,"name@domen.com")
        self.assertEqual(contact.birthday,"11-11-2011")
        
    
    def test_to_json(self):
        contact = Contact("name","077777777","name@domen.com","11-11-2011")
        contact_dict = contact.to_json()
        
        self.assertIsInstance(contact_dict,dict)
        
        self.assertEqual(contact_dict["name"],"name")
        self.assertEqual(contact_dict["phone_number"],"077777777")
        self.assertEqual(contact_dict["email_address"],"name@domen.com")
        self.assertEqual(contact_dict["birthday"],"11-11-2011")
    
    


if __name__ == '__main__':
    unittest.main()
    
        
        
    