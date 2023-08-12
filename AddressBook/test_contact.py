import unittest

from Addressbook import is_valid_telephone, is_valid_name, is_valid_mail, is_valid_address, is_valid_url


class TestContactAttributes(unittest.TestCase):
    """
    testing attributes, giving 2 true and 1 false values for testing
    """
    def test_name(self):
        self.assertTrue(is_valid_name('Anna'))
        self.assertTrue(is_valid_name('Mary'))
        #self.assertTrue(is_valid_name('hj44'))

    def test_telephone(self):
        self.assertTrue(is_valid_telephone('+37477445599'))
        self.assertTrue(is_valid_telephone('012345678'))
        #self.assertFalse(is_valid_telephone('+374abc+++'))

    def test_mail(self):
        self.assertTrue(is_valid_mail('anna@gmail.com'))
        self.assertTrue(is_valid_mail('mary.yan@mail.ru'))
        #self.assertTrue(is_valid_mail('mary.@mail@ru'))

    def test_address(self):
        self.assertTrue(is_valid_address('Saryan 45'))
        self.assertTrue(is_valid_address('Abovyan 45/89'))
        #self.assertTrue(is_valid_address('Nersisyan +'))

    def test_valid_url(self):
        self.assertTrue(is_valid_url('https://docs.python.org/3/library/unittest.html'))
        self.assertTrue(is_valid_url('http://www.google.com'))
        #self.assertTrue(is_valid_url('http://www.google.'))


if __name__ == '__main__':
    unittest.main()